// For Nav Bar Responsive Burger
const burger = document.getElementById('burger');
const navbarCenter = document.querySelector('.navbar-center');

burger.addEventListener('click', () => {
    navbarCenter.classList.toggle('active');
});


// For the About Section Image movement
document.addEventListener("DOMContentLoaded", function() {
    // Hide loader and show content once the page is fully loaded
    window.addEventListener("load", function() {
        var loaderWrapper = document.getElementById("loader-wrapper");
        loaderWrapper.style.display = "none";

        var content = document.getElementById("content");
        content.style.display = "block";
    });
});

// For Partners Scrolling
document.addEventListener('DOMContentLoaded', function() {
    const partnersButton = document.querySelector('#partners-button');

    if (partnersButton) {
        partnersButton.addEventListener('click', function(event) {
            const currentURL = window.location.href.split('#')[0];
            const targetURL = partnersButton.href.split('#')[0];

            if (currentURL === targetURL) {
                event.preventDefault(); // Prevent default anchor behavior

                const section4 = document.querySelector('#section4');
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const offset = section4.offsetTop - navbarHeight;

                // Scroll to the desired position smoothly
                window.scrollTo({
                    top: offset,
                    behavior: 'smooth'
                });
            }
            // If the URLs are different, the default anchor behavior will navigate to the target page
        });
    }
});


function toggleAdminDropdown(id) {
    const dropdownMenu = document.getElementById(`admin-dropdown-${id}`);
    dropdownMenu.classList.toggle('show');
}

window.onclick = function(event) {
    if (!event.target.matches('.admin-dropdown-toggle')) {
        const dropdowns = document.getElementsByClassName('admin-dropdown-menu');
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

