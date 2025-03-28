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

document.addEventListener('DOMContentLoaded', function() {
    const loadingOverlay = document.getElementById('loadingOverlay');
    const progressBar = document.getElementById('progressBar');
    const percentageText = document.getElementById('percentageText');
    let progress = 0;

    // غیرفعال کردن اسکرول و کلیک
    document.body.style.overflow = 'hidden';

    // شبیه‌سازی پیشرفت واقعی
    const simulateProgress = () => {
        const resources = performance.getEntriesByType('resource');
        const total = resources.length;
        const loaded = resources.filter(r => r.duration > 0).length;
        const realProgress = Math.min((loaded / total) * 100, 100);

        // به‌روزرسانی پیشرفت
        progress = Math.min(progress + 2, realProgress);
        progressBar.style.width = progress + '%';
        percentageText.textContent = Math.round(progress) + '%';

        if(progress < 100) {
            requestAnimationFrame(simulateProgress);
        }
    };

    // شروع فرآیند
    simulateProgress();

    // پایان بارگذاری
    window.addEventListener('load', () => {
        // تکمیل نوار پیشرفت
        progressBar.style.width = '100%';
        percentageText.textContent = '100%';

        // محو شدن پس از 500ms
        setTimeout(() => {
            loadingOverlay.style.opacity = '0';
            setTimeout(() => {
                loadingOverlay.remove();
                document.body.style.overflow = 'auto';
            }, 500);
        }, 500);
    });
});
