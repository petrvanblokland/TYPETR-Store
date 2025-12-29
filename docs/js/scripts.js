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
  const menu = document.getElementById("navbar");
  menu.style.display = (menu.style.display === "none") ? "block" : "none";
}


const popup = document.getElementById('popup');

window.addEventListener('click', function(event) {
if (event.target === popup) {
  popup.style.display = 'none';
}
});

const navbar = document.getElementById('navbar');

window.addEventListener('click', function(event) {
if (event.target === navbar) {
  navbar.style.display = 'none';
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

