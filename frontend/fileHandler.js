// FILE DROP HANDLER
let file = null;
const allowedFormats = [
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/msword"
]

// prevent loading file when drag and dropping file
window.addEventListener("drop", (e) => {
    e.preventDefault();
});

window.addEventListener("dragover", (e) => {
    e.preventDefault();
});

// add event listener for drag and drop
let dropzoneBox = document.getElementById("dropzoneBox");
dropzoneBox.addEventListener("drop", (e) => {
    if (!checkValidity(e.dataTransfer.items)) return;
    file = e.dataTransfer.items[0].getAsFile();
    displayUploadedFile();
});

let fileInput = document.getElementById("dropzone");
fileInput.addEventListener("change", (e) => {
    if (!checkValidity(e.target.files)) return;
    file = e.target.files[0];
    displayUploadedFile();
});

// HELPER FUNCTIONS FOR DROP HANDLERS

function displayUploadedFile() {
    document.getElementById("preUploadMessage").classList.toggle("hidden");
    let filename = document.getElementById("filename");
    filename.classList.toggle("hidden");
    filename.innerHTML = `Uploaded File: ${file.name}`;
    document.getElementById("dropzone").disabled = true;
}

// checks if input is correct
function checkValidity(fileList) {
    if (file !== null) return false;
    if (!fileList) return false;
    if (fileList.length !== 1) return false;
    if (fileList.constructor.name === "FileList") {
        // handler for FileList object
        if (!allowedFormats.includes(fileList[0].type)) return false;
    } else {
        // handler for DataTransferItemList object
        if (fileList[0]?.kind !== "file") return false;
        if (!allowedFormats.includes(fileList[0].getAsFile().type)) return false;
    }
    return true;
}