// script.js

// Function to handle smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        // Prevent default hash link behavior
        e.preventDefault();

        // Get the target element ID from the href attribute
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            // Use the smooth scroll behavior
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});