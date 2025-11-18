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
    let menu = document.querySelector('.navbar');
    menu.classList.toggle('active');
}

//document.addEventListener('DOMContentLoaded', function() {
//    showSlides();
//});


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

