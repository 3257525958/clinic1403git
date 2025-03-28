document.addEventListener("DOMContentLoaded", function () {
    let index = 0;
    const slides = document.querySelectorAll(".slide");

    function showSlides() {
        slides.forEach(slide => slide.style.display = "none");
        index++;
        if (index > slides.length) index = 1;
        slides[index - 1].style.display = "block";
        setTimeout(showSlides, 3000);
    }

    showSlides();

    // منو در حالت موبایل
    const menuIcon = document.querySelector('.menu-icon');
    const menu = document.querySelector('.menu');

    menuIcon.addEventListener('click', () => {
        menu.classList.toggle('open');
    });
});