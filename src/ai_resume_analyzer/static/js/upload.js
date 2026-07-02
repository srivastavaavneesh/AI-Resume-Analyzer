const fileInput = document.getElementById("file");
const browseBtn = document.getElementById("browse-btn");
const dropArea = document.getElementById("drop-area");
const fileInfo = document.getElementById("file-info");

browseBtn.addEventListener("click", () => {

    fileInput.click();

});

fileInput.addEventListener("change", updateFile);

dropArea.addEventListener("dragover", e => {

    e.preventDefault();

    dropArea.classList.add("dragover");

});

dropArea.addEventListener("dragleave", () => {

    dropArea.classList.remove("dragover");

});

dropArea.addEventListener("drop", e => {

    e.preventDefault();

    dropArea.classList.remove("dragover");

    fileInput.files = e.dataTransfer.files;

    updateFile();

});

function updateFile(){

    if(fileInput.files.length===0){

        fileInfo.textContent="No file selected";

        return;

    }

    const file=fileInput.files[0];

    const size=(file.size/1024/1024).toFixed(2);

    fileInfo.textContent=
        `${file.name} (${size} MB)`;

}

const form = document.getElementById("upload-form");
const overlay = document.getElementById("loading-overlay");
const submitBtn = document.getElementById("submit-btn");

form.addEventListener("submit", () => {

    submitBtn.disabled = true;

    submitBtn.innerText = "Analyzing...";

    overlay.classList.add("show");

});