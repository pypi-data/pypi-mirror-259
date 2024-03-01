from hashlib import md5
from django.utils.crypto import salted_hmac, constant_time_compare
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from django.conf import settings

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend

import hashlib
import os
import shutil
import zipfile

from typing import IO, Union

from .settings import (
    DUMP_MUST_NOT_ENCRYPT,
)

# MAGIC_BYTES = b"PK\x03\x04"
MAGIC_BYTES = b"\x0B4CKUP_\x0D\x0B" # BACKUP_DB
CHUNK_SIZE = 64 * 2**10 # 64 KiB
  
class InvalidDumpException(Exception):
    pass

class CryptoFailedException(Exception):
    pass

def _get_key(key=None, use_md5=True) -> bytes:
    if key is None:
        key = bytes(settings.SECRET_KEY, "utf-8")

    if use_md5:
        key = md5(key).digest()

    return key

def sign(key, value) -> bytes:
    s = salted_hmac("import_export.db.signature", value, secret=key, algorithm="sha256")
    return s.digest() # returns length of 32 (256 bits)


def is_valid_dump(file: File, key=None, fail_silently=True, strict=False, use_md5: bool=True) -> Union[bool, tuple[zipfile.ZipFile, bool]]:
    """
        Check if a file is a valid zipfile.
    """

    key = _get_key(key=key, use_md5=use_md5)

    f = file.open("rb")
    z = None
    magic_bytes = f.read(len(MAGIC_BYTES))
    if magic_bytes != MAGIC_BYTES:
        if strict and not DUMP_MUST_NOT_ENCRYPT:
            if not fail_silently:
                raise InvalidDumpException("Invalid magic bytes.")
            return None, False
        
        f.seek(0)
        z = zipfile.ZipFile(f, "r")
        if not z.testzip() is None:
            if not fail_silently:
                raise InvalidDumpException("Invalid zipfile.")
            return False
        return True
        
    else:
        f.seek(len(MAGIC_BYTES) + 16)
        signature = f.read(32)
        if not signature or len(signature) != 32:
            if not fail_silently:
                raise CryptoFailedException("Invalid signature.")
            return None, False
        
        hasher = hashlib.sha256()
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            hasher.update(chunk)

        cmp = sign(key, hasher.digest())
        if not constant_time_compare(signature, cmp):
            if not fail_silently:
                raise CryptoFailedException("Invalid signature.")
            return None, False
        f.seek(0)
        return f, True


def aes_encrypt_file(file: File, key: bytes=None, use_md5: bool=True) -> IO[bytes]:
    """
        Encrypt a file with AES.
    """

    if DUMP_MUST_NOT_ENCRYPT:
        return file

    key = _get_key(key=key, use_md5=use_md5)

    # Generate random IV for AES block cipher
    iv = os.urandom(16)

    # Generate AES cipher
    cipher = Cipher(
        algorithms.AES(key), 
        modes.CBC(iv), 
        backend=default_backend()
    )

    # Create encryptor (Generator for encrypting data)
    encryptor = cipher.encryptor()

    padder = PKCS7(algorithms.AES.block_size).padder()
    file_hash = hashlib.sha256()

    # Write data to temporary file
    temp_file = NamedTemporaryFile(suffix=".aes")
    signed_temp_file = NamedTemporaryFile(suffix=".aes")
    with open(temp_file.name, "r+b") as unsigned, open(signed_temp_file.name, "wb") as signed:
        signed.write(MAGIC_BYTES)
        signed.write(iv)

        file.DEFAULT_CHUNK_SIZE = CHUNK_SIZE
        
        for chunk in file.chunks():
            data = padder.update(chunk)
            data = encryptor.update(data)
            file_hash.update(data)
            unsigned.write(data)

            
        data = padder.finalize()
        data = encryptor.update(data)
        file_hash.update(data)
        unsigned.write(data)

        data = encryptor.finalize()
        file_hash.update(data)
        unsigned.write(data)

        # Seek back to 0 to read out all encrypted data
        unsigned.seek(0)

        # Sign file
        signature = sign(key, file_hash.digest())
        signed.write(signature)

        # Copy unsigned file to signed file
        shutil.copyfileobj(unsigned, signed)

    # Return temporary file as django File object
    return File(signed_temp_file, name=file.name)


def aes_decrypt_file(file: File, key: bytes=None, use_md5: bool=True, is_safe: bool = False) -> IO[bytes]:
    """
        Decrypt a file with AES.
    """

    if DUMP_MUST_NOT_ENCRYPT:
        # check for magic
        magic_bytes = file.read(len(MAGIC_BYTES))
        if magic_bytes != MAGIC_BYTES:
            file.seek(0)
            return file

    key = _get_key(key=key, use_md5=use_md5)

    # Unpadder for removing padding
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()

    with file.open("rb") as zip_file:

        # Read magic bytes
        magic_bytes = zip_file.read(len(MAGIC_BYTES))
        if magic_bytes != MAGIC_BYTES:
            raise InvalidDumpException("Invalid magic bytes.")

        # Read IV from file
        iv = zip_file.read(16)
        
        # Read signature
        signature = zip_file.read(32)

        if not signature or len(signature) != 32:
            raise CryptoFailedException("Invalid signature.")

        # Initialize AES cipher
        cipher = Cipher(
            algorithms.AES(key), 
            modes.CBC(iv), 
            backend=default_backend()
        )

        # Create decryptor (Generator for decrypting data)
        decryptor = cipher.decryptor()
        hasher = hashlib.sha256()

        # Write encrypted data to (unencrypted) temporary file
        temp_file = NamedTemporaryFile()
        with open(temp_file.name, "wb") as f:
            while True:
                chunk = zip_file.read(CHUNK_SIZE)
                if not chunk:
                    break
                hasher.update(chunk)
                data = decryptor.update(chunk)
                data = unpadder.update(data)
                f.write(data)

            data = decryptor.finalize()
            data = unpadder.update(data)
            f.write(data)

            data = unpadder.finalize()
            f.write(data)

            # Check signature
            cmp = sign(key, hasher.digest())
            if not constant_time_compare(signature, cmp):
                raise CryptoFailedException("Invalid signature.")

    return File(temp_file, name=file.name)
