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

// JavaScript for toggling the mobile menu
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobile-nav');
const closeBtn = document.getElementById('close-btn');

// Open the mobile nav when the hamburger is clicked
hamburger.addEventListener('click', () => {
  mobileNav.classList.add('open');
  document.body.classList.add('no-scroll'); // Disable scrolling
});

// Close the mobile nav when the close button is clicked
closeBtn.addEventListener('click', () => {
  mobileNav.classList.remove('open');
  document.body.classList.remove('no-scroll'); // Enable scrolling

});


document.getElementById("gallery").addEventListener("click", function() {
  alert("Gallery coming soon!");
});