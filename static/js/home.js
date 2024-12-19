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