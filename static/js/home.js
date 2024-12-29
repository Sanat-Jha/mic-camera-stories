// Helper function to format numbers to 'k' notation
function formatNumberToK(number) {
    if (number >= 1000) {
      return (number / 1000).toFixed(1).replace(/\.0$/, '') + 'k+';
    }
    return number;
  }
  
  // Example data (replace these with dynamic values from your backend)

  
  // Update the views and subscribers elements with formatted numbers
  document.getElementById('total-views').innerText = formatNumberToK(views);
  document.getElementById('total-subscribers').innerText = formatNumberToK(subscribers);
  

    // Get all video containers (both from trending and more videos)
    const videoContainers = document.querySelectorAll('.video-container');

    // Add click event to each video container
    videoContainers.forEach(container => {
      container.addEventListener('click', () => {
        // Get video ID from data attribute
        const videoId = container.getAttribute('data-video-id');
        
        // Redirect to /story with the video ID as a query parameter
        window.location.href = `/story?videoid=${videoId}`;
      });
    });


    // Add this to your existing home.js file
document.addEventListener('DOMContentLoaded', () => {
  // Function to check if element is in viewport with offset
  function isElementInViewport(el, offset = 0) {
    const rect = el.getBoundingClientRect();
    return (
      rect.top <= (window.innerHeight - offset) &&
      rect.bottom >= 0
    );
  }

  // Function to check if element has left viewport
  function hasElementLeftViewport(el, offset = 0) {
    const rect = el.getBoundingClientRect();
    return (
      rect.bottom <= 0 || // scrolled past top
      rect.top >= window.innerHeight // scrolled past bottom
    );
  }

  // Elements to animate
  const animatedElements = {
    '.headlinetext': { growScale: 1, shrinkScale: 0.5 },
    '.homemicimage': { growScale: 1, shrinkScale: 0.7 },
    '.yourstoryvideo': { growScale: 1.05, shrinkScale: 0.9 },
    '.channeldataitem': { growScale: 1.1, shrinkScale: 0.8 }
  };

  // Handle scroll animation
  function handleScrollAnimation() {
    Object.entries(animatedElements).forEach(([selector, scales]) => {
      const elements = document.querySelectorAll(selector);
      elements.forEach(element => {
        if (isElementInViewport(element, 100)) {
          element.style.transform = `scale(${scales.growScale})`;
          element.style.opacity = '1';
        } else if (hasElementLeftViewport(element, 100)) {
          element.style.transform = `scale(${scales.shrinkScale})`;
          element.style.opacity = '0';
        }
      });
    });
  }

  // Add scroll event listener with debounce
  let scrollTimeout;
  window.addEventListener('scroll', () => {
    if (scrollTimeout) {
      window.cancelAnimationFrame(scrollTimeout);
    }
    scrollTimeout = window.requestAnimationFrame(() => {
      handleScrollAnimation();
    });
  });

  // Initial check
  handleScrollAnimation();
});
  

    