const dropZone = document.getElementById("dropZone");
const imageInput = document.getElementById("imageInput");
const zoneContent = document.getElementById("zoneContent");
const preview = document.getElementById("preview");
const detectBtn = document.getElementById("detectBtn");
const metricsDashboard = document.getElementById("metricsDashboard");
const predictionOutcome = document.getElementById("predictionOutcome");
const analysisSpinner = document.getElementById("analysisSpinner");
const historyList = document.getElementById("historyList");

// SVG Circle Constants for Gauge Calculation
const circle = document.getElementById("gaugeCircle");
const radius = circle.r.baseVal.value;
const circumference = radius * 2 * Math.PI;

// Configure SVG properties based on geometry calculations
circle.style.strokeDasharray = `${circumference} ${circumference}`;
circle.style.strokeDashoffset = circumference;

// Execution Context History Stack
let trackingHistory = [];

/* UI State Controls */
function setCircularGauge(percentage, colorHex) {
    const offset = circumference - (percentage / 100) * circumference;
    circle.style.stroke = colorHex;
    circle.style.strokeDashoffset = offset;
    document.getElementById("gaugeValue").innerText = `${Math.round(percentage)}%`;
}

/* Event Management Matrix for Drag-and-Drop functionality */
dropZone.addEventListener("click", () => imageInput.click());

['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.add('drag-over');
    }, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.remove('drag-over');
    }, false);
});

dropZone.addEventListener("drop", (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length) {
        imageInput.files = files;
        renderPreview(files[0]);
    }
});

imageInput.addEventListener("change", () => {
    if (imageInput.files.length) renderPreview(imageInput.files[0]);
});

function renderPreview(file) {
    if (preview.src && preview.src.startsWith("blob:")) {
        URL.revokeObjectURL(preview.src);
    }
    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";
    zoneContent.style.display = "none";
    metricsDashboard.style.display = "none";
}

/* REST API Network Pipeline Wrapper */
detectBtn.addEventListener("click", async (event) => {
    event.preventDefault();
    const file = imageInput.files[0];

    if (!file) {
        alert("Verification error: No image specimen loaded.");
        return;
    }

    // Toggle states to loading mode
    detectBtn.disabled = true;
    analysisSpinner.style.display = "block";
    metricsDashboard.style.display = "none";

    const formData = new FormData();
    formData.append("file", file);

    try {
        // Switch out url with production endpoints post-deployment 
        const response = await fetch("https://deepshield-deepfake-detection.onrender.com/predict", {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error(`HTTP network fault code: ${response.status}`);

        const data = await response.json();
        
        const prediction = data.prediction || "UNKNOWN";
        const confidence = data.confidence !== undefined ? data.confidence : 0;
        const color = prediction.toUpperCase() === "REAL" ? "#10b981" : "#ef4444";

        // Display dashboard contents safely
        analysisSpinner.style.display = "none";
        metricsDashboard.style.display = "flex";
        
        predictionOutcome.innerText = prediction.toUpperCase();
        predictionOutcome.style.color = color;
        
        setCircularGauge(confidence, color);
        pushHistoryStack(file.name, prediction, confidence, color);

    } catch (error) {
        console.error(error);
        analysisSpinner.style.display = "none";
        alert(`Analysis halted: ${error.message}`);
    } finally {
        detectBtn.disabled = false;
    }
});

/* Update History Queue View */
function pushHistoryStack(filename, result, score, color) {
    trackingHistory.unshift({ filename, result, score, color });
    if (trackingHistory.length > 3) trackingHistory.pop(); // Cap history length at 3 elements

    historyList.innerHTML = "";
    trackingHistory.forEach(item => {
        const li = document.createElement("li");
        li.className = "history-item";
        li.innerHTML = `
            <span>${item.filename}</span>
            <span style="color:${item.color}; font-weight:700;">${item.result} (${item.score}%)</span>
        `;
        historyList.appendChild(li);
    });
}