function downloadFile(data, csrf_token) {
    let filename = data.filename
    let url = data.url
    fetch(url, {
        method: "GET",
        headers: {
            "X-CSRFToken": csrf_token,
            "Content-Type": "application/json"
        },
    }).then(function(response) {
        return response.blob()
    }).then(function(blob) {
        let url = window.URL.createObjectURL(blob)
        let a = document.createElement('a')
        a.style.display = 'none'
        a.href = url
        a.download = filename
        document.body.appendChild(a)
        a.click()
        a.remove()
    }).catch(function(error) {
        console.error("There has been a problem with your fetch operation: ", error.error)
    })
}

function addDumpResult(data) {
    let template = document.getElementById("dump-template")
    let clone = template.content.cloneNode(true)
    let tr = clone.querySelector("tr")
    let innerHTML = tr.innerHTML
    innerHTML = innerHTML.replace("__DATABASE__", data.database)
    innerHTML = innerHTML.replace("__TABLES_COUNT__", data.tables.length)
    innerHTML = innerHTML.replace("__DUMP_FILESIZE__", data.filesize)
    innerHTML = innerHTML.replace("__DUMP_CREATED__", data.created)
    innerHTML = innerHTML.replace("__DOWNLOAD_URL__", data.url)
    innerHTML = innerHTML.replace("__RECOVER_URL__", data.recover_url)
    innerHTML = innerHTML.replace("__EDIT_URL__", data.edit_url)
    tr.innerHTML = innerHTML

    let tbody = document.querySelector(".listing-items")
    if (tbody) {
        if (tbody.children.length > 0) {
            tbody.insertBefore(tr, tbody.children[0])
            tbody.lastElementChild.remove()
        } else {
            tbody.appendChild(tr)
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    let exportButton = document.getElementById("export_database")
    let import_export_post_url = exportButton.dataset.selectedDatabaseUrl
    let import_export_exporting_text = exportButton.dataset.exportingText
    let import_export_export_text = exportButton.dataset.exportText
    let import_export_csrf_token = exportButton.dataset.csrfToken
    let bar = document.getElementById("bar")
    exportButton.addEventListener("click", function() {
        exportButton.disabled = true
        exportButton.innerHTML = import_export_exporting_text
        exportButton.classList.add("button-longrunning-active")
        bar.style.width = "0%"
        bar.innerHTML = ""
        fetch(import_export_post_url, {
            method: "POST",
            headers: {
                "X-CSRFToken": import_export_csrf_token,
                "Content-Type": "application/json"
            },
        }).then(function(response) {
            bar.style.width = "50%"
            return response.json()
        }).then(function(data) {
            bar.style.width = "100%"
            exportButton.innerHTML = import_export_export_text
            exportButton.disabled = false
            exportButton.classList.remove("button-longrunning-active")
            if (data.error) {
                throw new Error(data.error)
            }
            let span = document.createElement("span")
            span.href = data.url
            span.target = "_blank"
            span.style.color = "white"
            span.style.textDecoration = "underline"
            span.style.cursor = "pointer"
            span.innerHTML = data.filename
            bar.appendChild(span)

            try {
                addDumpResult(data)
            } catch (error) {
                console.error("There has been a problem with your fetch operation, could not append dump result: ", error.error)
            }

            downloadButton = document.getElementById("download_export")
            downloadButton.parentElement.style.display = "block"
            downloadButton.addEventListener("click", function() {
                downloadFile(data, import_export_csrf_token) 
            })
            span.addEventListener("click", function() {
                downloadFile(data, import_export_csrf_token) 
            })
        }).catch(function(error) {
            exportButton.innerHTML = import_export_export_text
            exportButton.disabled = false
            console.error("There has been a problem with your fetch operation: ", error.error)
        })
    })

});
