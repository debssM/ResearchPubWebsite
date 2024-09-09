$(document).ready(function() {
        // Debugging: Check if images are loaded
        $('img').on('error', function() {
            console.error('Image not found:', this.src);
        });

        // Initialize Panzoom for each image
        $('.image-container').each(function() {
            const img = this.querySelector('div');
            if (img) {
                try {
                    const panzoom = new Panzoom(img, {
                        contain: 'outside',
                        cursor: 'move'
                    });
                    // Add click interaction to enable/disable panzoom on click
                    $(this).on('click', function() {
                        if (panzoom.getScale() === 1) {
                            panzoom.zoomIn(); // Zoom in on click
                        } else {
                            panzoom.reset(); // Reset to original state if already zoomed
                        }
                    });
                } catch (error) {
                    console.error('Panzoom initialization error:', error);
                }
            } else {
                console.error('No image found in container:', this);
            }
        });
    });
