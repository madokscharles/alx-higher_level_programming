// Start by waiting for the document to be ready
$(document).ready(function() {
    const redHeader = $("#red_header");
    // Adding click event handler
    redHeader.click(function() {
        const headerColor = $("header");
        // Changing color to red
        headerColor.css("color", "#FF0000");
    });
});
