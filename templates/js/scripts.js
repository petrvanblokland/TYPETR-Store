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


//scroll in-page link - change color

document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll("section.content[id]");
    const navLinks = document.querySelectorAll(".sectionNavList a");

    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;

                const id = entry.target.id;

                navLinks.forEach(link => link.classList.remove("active"));

                document
                    .querySelectorAll(`.sectionNavList a[href="#${id}"]`)
                    .forEach(link => link.classList.add("active"));
            });
        },
        {
            root: null,
            threshold: 0,
            rootMargin: "0px 0px -60% 0px"
        }
    );

    sections.forEach(section => observer.observe(section));
});

