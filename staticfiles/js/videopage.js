  
  // Wait for the DOM to fully load
  document.addEventListener('DOMContentLoaded', function() {

    // Select the share icon
    const shareButton = document.querySelector('.share');
    
    // Check if the shareButton exists
    if (shareButton) {
    
      // Add a click event listener to the share button
      shareButton.addEventListener('click', function(e) {
        
        // Prevent default action
        e.preventDefault();
        
        // Get the current page URL
        const pageUrl = window.location.href;
    
    
          navigator.share({
            title: document.title, // Share the page title
            url: pageUrl, // Share the current URL
          }).then(() => {
            console.log('Page shared successfully');
          }).catch((error) => {
            console.error('Error sharing:', error);
          });
        
      });
    }
    
    });


    // Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {

  // Function to convert large numbers to "k+" format
  function formatNumber(number) {
    if (number >= 1000) {
      return (number / 1000).toFixed(1) + 'k'; // Divide by 1000 and append "k+" with one decimal
    }
    return number; // Return the number as-is if less than 1000
  }

  // Select the elements where the views and likes are displayed
  const viewElements = document.querySelectorAll('.view .stats');
  const likeElements = document.querySelectorAll('.like .stats');

  // Convert the views count to k+ format
  viewElements.forEach(element => {
    const views = parseInt(element.textContent.replace(/[^0-9]/g, '')); // Remove any non-numeric characters
    element.textContent = formatNumber(views); // Update the element text with the formatted value
  });

  // Convert the likes count to k+ format
  likeElements.forEach(element => {
    const likes = parseInt(element.textContent.replace(/[^0-9]/g, '')); // Remove any non-numeric characters
    element.textContent = formatNumber(likes); // Update the element text with the formatted value
  });

});
