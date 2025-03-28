document.addEventListener('DOMContentLoaded', function () {
  // اسلایدر تصاویر
  const slides = document.querySelectorAll('.carousel .carousel-item');
  let currentSlide = 0;
  setInterval(() => {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
  }, 4000);

  // آپلود تصویر پروفایل
  const profileUpload = document.querySelector('.profile-upload');
  const profileInput = document.getElementById('profilePicInput');

  profileUpload.addEventListener('click', () => {
    profileInput.click();
  });

  profileInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        profileUpload.innerHTML = '<img src="' + e.target.result + '" alt="تصویر کاربر">';
      };
      reader.readAsDataURL(file);
    }
  });

  // نوار پیشرفت بارگذاری
  const progressBar = document.getElementById('progressBar');
  const progressOverlay = document.getElementById('progressOverlay');
  let progress = 0;
  const progressInterval = setInterval(() => {
    progress += 5;
    if (progress >= 100) {
      progress = 100;
      clearInterval(progressInterval);
      progressOverlay.classList.add('hidden');
    }
    progressBar.style.width = progress + '%';
  }, 200);
});