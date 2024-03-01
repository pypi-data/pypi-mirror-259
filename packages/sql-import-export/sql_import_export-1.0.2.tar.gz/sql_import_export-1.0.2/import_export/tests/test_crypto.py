from unittest import TestCase
from ..crypto import (
    aes_encrypt_file,
    aes_decrypt_file,
)

class FakeFile:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def open(self, mode: str) -> 'FakeFile':
        return self
    
    def read(self, size: int = -1) -> bytes:
        if size == -1:
            size = len(self.data)

        initial_pos = self.pos
        self.pos += size
        return self.data[initial_pos:self.pos]
    
    def seek(self, offset: int, whence: int=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = len(self.data) + offset

    def tell(self):
        return self.pos

    def close(self):
        pass

# Create your tests here.
class CryptoFileTest(TestCase):
    def test_crypto_file(self):
        data = b"Hello, World!"
        file = FakeFile(data)
        encrypted = aes_encrypt_file(file, key="test_key")
        decrypted = aes_decrypt_file(encrypted, key="test_key")

        self.assertNotEqual(data, encrypted)
        self.assertEqual(data, decrypted.read(len(data)))
        