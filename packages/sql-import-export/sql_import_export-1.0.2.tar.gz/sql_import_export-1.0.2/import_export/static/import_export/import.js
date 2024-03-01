document.addEventListener("DOMContentLoaded", function() {
    let databaseZipInput = document.getElementById("database-zip-input");
    let databaseZipInputFile = document.getElementById("database-zip-input-file");
    const uploadURL = databaseZipInput.dataset.uploadUrl;
    const csrfToken = databaseZipInput.dataset.csrfToken;


    databaseZipInput.addEventListener("dragover", function(event) {
        event.preventDefault();
        databaseZipInput.classList.add("dragover");
    });
    databaseZipInput.addEventListener("dragleave", function(event) {
        event.preventDefault();
        databaseZipInput.classList.remove("dragover");
    });
    databaseZipInput.addEventListener("drop", function(event) {
        event.preventDefault();
        databaseZipInput.classList.remove("dragover");
        let files = event.dataTransfer.files;
        uploadFiles(files);
    }, false);

    databaseZipInputFile.addEventListener("change", function(event) {
        let files = event.target.files;
        uploadFiles(files);
    });

    function uploadFiles(files) {
        if (files.length > 1) {
            alert("You can only upload one file at a time.");
            return;
        }
        console.log("Sending file to server..."); // DEBUG
        let formData = new FormData();
        formData.append("file", files[0]);
        let uploadProgress = document.querySelector("#upload-progress .bar");
        uploadProgress.style.width = "0%";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", uploadURL, true);
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xhr.timeout = 1000 * 60 * 30 // 30 minutes
        xhr.upload.addEventListener("progress", function(event) {
            if (event.lengthComputable) {
                let percentComplete = event.loaded / event.total;
                uploadProgress.style.width = percentComplete * 80 + "%";
            }
        });
        try {
            xhr.addEventListener("load", function(event) {
                if (xhr.status == 200) {
                    let response = JSON.parse(xhr.responseText);
                    uploadProgress.style.width = "100%";
                    console.log("File uploaded successfully.", response); // DEBUG
                    let nextURL = response.next_url;
                    
                    window.location.href = nextURL;
                } else {
                    try {
                        let response = JSON.parse(xhr.responseText);
                        alert(response.error);
                    } catch (error) {
                        uploadProgress.style.width = "0%";
                        alert("An error occurred while uploading the file.");
                    }
                }
            });
            xhr.send(formData);
        } catch (error) {
            alert("An error occurred while uploading the file.");
        }
    }
});

