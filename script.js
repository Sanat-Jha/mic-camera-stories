// IntersectionObserver to trigger animation on scroll
const elements = document.querySelectorAll('.animate-on-scroll');

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Add the 'in-view' class to trigger the animation
      entry.target.classList.add('in-view');
      observer.unobserve(entry.target); // Stop observing once it triggers
    }
  });
}, { threshold: 0.5 }); // Trigger when 50% of the element is visible

elements.forEach(element => {
  observer.observe(element); // Start observing each element
});
