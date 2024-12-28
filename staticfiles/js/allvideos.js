


document.addEventListener('DOMContentLoaded', () => {
    // Options for the observer
    const options = {
      root: null, // Using the viewport
      rootMargin: '0px',
      threshold: 0.5, // 50% of the element must be visible
    };
  
    // Callback function to execute when intersection occurs
    const animateOnScroll = (entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Add animation classes when the element is visible
          entry.target.classList.add('visible');
  
          // Trigger different animations for each element
          if (entry.target.classList.contains('video-card')) {
            entry.target.classList.add('fade-in'); // fade-in effect
          } else if (entry.target.classList.contains('video-title')) {
            entry.target.classList.add('slide-in-left'); // slide in from left
          } else if (entry.target.classList.contains('video-stats')) {
            entry.target.classList.add('slide-in-right'); // slide in from right
          } else if (entry.target.classList.contains('watch-button')) {
            entry.target.classList.add('bounce-in'); // bounce-in effect
          }
          else if (entry.target.classList.contains('heading')) {
            entry.target.classList.add(''); // bounce-in effect
          }
  

  
          if (entry.target.classList.contains('footer')) {
            entry.target.classList.add('visible');
            entry.target.classList.add('slide-in-right');
          }
        }
      });
    };
  
    // Create an IntersectionObserver instance
    const observer = new IntersectionObserver(animateOnScroll, options);
  
    // Target all elements that should animate on scroll
    const elementsToAnimate = document.querySelectorAll(
      '.video-card, .video-title, .video-stats, .watch-button'
    );
  
    elementsToAnimate.forEach(element => {
      observer.observe(element);
    });
  });
  