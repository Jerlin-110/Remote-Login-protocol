// Ensure the script is executed after DOM content is loaded
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("download").addEventListener("click", fetchAlgo);
});

// Function to fetch `algo` value from the backend
function fetchAlgo() {
    const userId = localStorage.getItem("userId"); // Retrieve ID from localStorage

    if (!userId) {
        alert("User ID is not set in localStorage.");
        console.error("User ID is not set.");
        return;
    }

    fetch(`http://localhost:3000/fetch-algo?id=${userId}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            console.log(`Algo value for ID ${userId}: ${data.algo}`);
            document.getElementById("algo").textContent = data.algo; // Update the UI
            alert(`Algo value: ${data.algo}`);
            document.getElementById("userid").textContent = userId;
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("Failed to fetch algo value. Please try again.");
        });
}
