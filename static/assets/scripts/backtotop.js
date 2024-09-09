document.addEventListener('DOMContentLoaded', function () {
            var backToTopButton = document.getElementById('backToTop');

            // Show button when scrolled down 100px from the top
            window.addEventListener('scroll', function () {
                if (window.scrollY > 100) {
                    backToTopButton.style.display = 'block';
                } else {
                    backToTopButton.style.display = 'none';
                }
            });

            // Scroll to top when button is clicked
            backToTopButton.addEventListener('click', function () {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        });