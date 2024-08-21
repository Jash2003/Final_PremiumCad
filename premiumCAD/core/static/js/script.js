//Typing effect from typed js
var typed = new Typed(".auto-type", {
  strings: ["CAD Services", "GIS Solutions", "Solar Designs", "Telecom Services"],
  typeSpeed: 50,
  backSpeed: 50,
  loop: true
});

//Counters
const counters = document.querySelectorAll(".counters span");
const container = document.querySelector(".counters");
//Variable that tracks counter activation
let activated = false;
//scroll event
window.addEventListener("scroll", () => {
  if(
      pageYOffset > container.offsetTop - container.offsetHeight - 550 && activated === false
  ) {
      counters.forEach(counter => {
          counter.innerText = 0;
          let count = 0;

          function updateCount() {
              const target = parseInt(counter.dataset.count);
              if(count < target) {
                  count++;
                  counter.innerText = count;
                  setTimeout(updateCount, 1);
              }
              else {
                  counter.innerText = target;
              }
          }
          updateCount();
          activated = true;
      });
  }
});


//nav functionality

let lastScrollTop = 0;
const navbar = document.querySelector('nav');
const firstSection = document.querySelector('.first-section'); // Make sure to add a class to your first section

window.addEventListener('scroll', () => {
let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
let firstSectionHeight = firstSection.offsetHeight;

if (scrollTop > lastScrollTop && scrollTop > firstSectionHeight) {
  // Scroll down and past the first section
  navbar.classList.remove('showing');
  navbar.classList.add('hidden');
} else if (scrollTop < lastScrollTop && scrollTop > firstSectionHeight) {
  // Scroll up and past the first section
  navbar.classList.remove('hidden');
  navbar.classList.add('showing');
} else if (scrollTop <= firstSectionHeight) {
  // In the first section, always show the navbar
  navbar.classList.remove('hidden');
  navbar.classList.add('showing');
}

lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For mobile or negative scrolling
});


// careers page
