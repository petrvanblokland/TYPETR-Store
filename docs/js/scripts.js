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
  if (window.scrollY >= 300) {
    nav.classList.add('is-visible');
  } else {
    nav.classList.remove('is-visible');
  }
});


//scroll in-page link 

document.addEventListener("DOMContentLoaded", function() {
    // Selecteer alle secties met een id
    const sections = document.querySelectorAll('section.content[id]');
    // Selecteer alle navigatie-links
    const navLinks = document.querySelectorAll('.sectionNavList a');

    const observerOptions = {
        root: null, // viewport
        rootMargin: '0px',
        threshold: 0.5 // 50% van sectie zichtbaar
    };

    const observerCallback = (entries) => {
        entries.forEach(entry => {
            const id = entry.target.getAttribute('id');
            // Zoek alle links met deze href
            const links = document.querySelectorAll(`.sectionNavList a[href="#${id}"]`);

            if (entry.isIntersecting) {
                // Verwijder active van alle links
                navLinks.forEach(link => link.classList.remove('active'));
                // Voeg active toe aan links die bij deze sectie horen
                links.forEach(link => link.classList.add('active'));
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);
    sections.forEach(section => observer.observe(section));
});

