// -----------------------------------------------------------------------------
// File: upload.js
// Purpose: Handles file upload interactions (browse, drag & drop), displays
//          file info, and manages form submission with loading overlay.
// -----------------------------------------------------------------------------

const fileInput = document.getElementById("file");
const browseBtn = document.getElementById("browse-btn");
const dropArea = document.getElementById("drop-area");
const fileInfo = document.getElementById("file-info");

// Trigger file input when browse button is clicked
browseBtn.addEventListener("click", () => {
    fileInput.click();
});

// Update file info when a file is selected
fileInput.addEventListener("change", updateFile);

// Highlight drop area on drag over
dropArea.addEventListener("dragover", e => {
    e.preventDefault();
    dropArea.classList.add("dragover");
});

// Remove highlight when dragging leaves the area
dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("dragover");
});

// Handle file drop
dropArea.addEventListener("drop", e => {
    e.preventDefault();
    dropArea.classList.remove("dragover");
    fileInput.files = e.dataTransfer.files;
    updateFile();
});

// Update file info display
function updateFile() {
    if (fileInput.files.length === 0) {
        fileInfo.textContent = "No file selected";
        return;
    }
    const file = fileInput.files[0];
    const size = (file.size / 1024 / 1024).toFixed(2);
    fileInfo.textContent = `${file.name} (${size} MB)`;
}

// Handle form submission with loading overlay
const form = document.getElementById("upload-form");
const overlay = document.getElementById("loading-overlay");
const submitBtn = document.getElementById("submit-btn");

form.addEventListener("submit", () => {
    submitBtn.disabled = true;
    submitBtn.innerText = "Analyzing...";
    overlay.classList.add("show");
});
