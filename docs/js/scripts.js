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

const menuBox = document.getElementById('menuBox');
const BREAKPOINT = 767; // pas aan naar wens

function updateMenuVisibility() {
  if (window.innerWidth >= BREAKPOINT) {
    menuBox.style.display = 'none';
  }
}

window.addEventListener('resize', updateMenuVisibility);
window.addEventListener('load', updateMenuVisibility);

window.addEventListener('click', function (event) {
  if (event.target === menuBox) {
    menuBox.style.display = 'none';
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

