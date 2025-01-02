// script.js
document.addEventListener("DOMContentLoaded", function () {
    const serviceItems = document.querySelectorAll(".list-group-item");
    
    serviceItems.forEach(item => {
        item.addEventListener("mouseover", () => {
            item.style.backgroundColor = "#f1f1f1";
        });
        
        item.addEventListener("mouseout", () => {
            item.style.backgroundColor = "";
        });
    });
});