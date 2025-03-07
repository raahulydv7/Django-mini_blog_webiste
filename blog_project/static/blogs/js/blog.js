// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    console.log("Profile JS loaded successfully!");
    
    // Initialize Bootstrap toasts
    const toastElList = document.querySelectorAll('.toast');
    if (toastElList.length > 0) {
        toastElList.forEach(toastEl => {
            const toast = new bootstrap.Toast(toastEl, { delay: 10000 });
            toast.show();
        });
    }
    
    // Initialize upload menu button
    const uploadLabel = document.querySelector(".upload-label");
    if (uploadLabel) {
        uploadLabel.addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            toggleMenu();
        });
    }
    
    // Close menu when clicking outside
    document.addEventListener("click", function (event) {
        const menu = document.getElementById("uploadMenu");
        const button = document.querySelector(".upload-label");
        
        if (menu && button && !menu.contains(event.target) && !button.contains(event.target)) {
            menu.style.display = "none";
        }
    });
    
    // Set up file input change handler
    const fileInput = document.getElementById("profile_picture");
    if (fileInput) {
        fileInput.addEventListener("change", previewImage);
    }
    
    // Set up remove profile button
    const removeButton = document.querySelector("#uploadMenu button:nth-child(2)");
    if (removeButton) {
        removeButton.addEventListener("click", removeProfile);
    }
});

// Toggle upload menu visibility
function toggleMenu() {
    console.log("Toggle menu called");
    const menu = document.getElementById("uploadMenu");
    if (menu) {
        menu.style.display = (menu.style.display === "flex") ? "none" : "flex";
    }
}

// Preview uploaded image
function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            const profileImg = document.querySelector(".profile-img");
            if (profileImg) {
                profileImg.src = reader.result;
            }
        };
        reader.readAsDataURL(file);
        
        // Hide upload menu after selecting an image
        const menu = document.getElementById("uploadMenu");
        if (menu) {
            menu.style.display = "none";
        }
    }
}

// Remove profile image
function removeProfile() {
    const profileImg = document.querySelector(".profile-img");
    if (profileImg) {
        // Set to default image
        profileImg.src = "defulat.jpg"; // Update this path to your default image
        
        // Clear the file input
        const fileInput = document.getElementById("profile_picture");
        if (fileInput) {
            fileInput.value = "";
        }
        
        // Hide the menu
        const menu = document.getElementById("uploadMenu");
        if (menu) {
            menu.style.display = "none";
        }
    }
}