// Function to reload the page after 30 seconds
function reloadPage() {
    setTimeout(function() {
        location.reload();
    }, 30000);  // 30 seconds in milliseconds
}

// Call reloadPage() function when the page loads
window.onload = function() {
    reloadPage();
};




