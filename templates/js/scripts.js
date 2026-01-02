let slideIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll('.slide');

    slides.forEach((slide, index) => {
        slide.style.opacity = "0";
        slide.style.zIndex = "0";
        slide.classList.remove("active");
    });

    slideIndex = (slideIndex + 1) % slides.length;

    const currentSlide = slides[slideIndex];
    currentSlide.style.opacity = "1";
    currentSlide.style.zIndex = "1";
    currentSlide.classList.add("active");

    setTimeout(showSlides, 3000);
}

function toggleMenu() {
  const menu = document.getElementById("menuBox");
  menu.style.display = (menu.style.display === "none") ? "block" : "none";
}


//Popup 


const popup = document.getElementById('popup');

window.addEventListener('click', function(event) {
if (event.target === popup) {
  popup.style.display = 'none';
}
});


//menuBox 

const box = document.getElementById('box');
const BREAKPOINT = 767; // pas aan naar wens

function updateMenuVisibility() {
  if (window.innerWidth >= BREAKPOINT) {
    box.style.display = 'none';
  }
}

window.addEventListener('resize', updateMenuVisibility);
window.addEventListener('load', updateMenuVisibility);

window.addEventListener('click', function (event) {
  if (event.target === box) {
    box.style.display = 'none';
  }
});

//sticky 

const nav = document.querySelector('.sectionNav');

window.addEventListener('scroll', () => {
  if (window.scrollY >= 600) {
    nav.classList.add('is-visible');
  } else {
    nav.classList.remove('is-visible');
  }
});


const sections = document.querySelectorAll('section.content[id]');
const navLinks = document.querySelectorAll('.sectionNavList a');

const observerOptions = {
  root: null, // viewport
  rootMargin: '0px',
  threshold: 0.5 // 50% van de sectie zichtbaar
};

// Callback functie voor observer
const observerCallback = (entries) => {
  entries.forEach(entry => {
    const id = entry.target.getAttribute('id');
    const link = document.querySelector(`.sectionNavList a[href="#${id}"]`);

    if (entry.isIntersecting) {
      // Verwijder active van alle links
      navLinks.forEach(l => l.classList.remove('active'));
      // Voeg toe aan de link die zichtbaar is
      if (link) link.classList.add('active');
    }
  });
};

// Maak observer
const observer = new IntersectionObserver(observerCallback, observerOptions);

// Observeer elke sectie
sections.forEach(section => observer.observe(section));

