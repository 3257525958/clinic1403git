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

// document.addEventListener('DOMContentLoaded', function() {
//     const loadingOverlay = document.getElementById('loadingOverlay');
//     const progressBar = document.getElementById('progressBar');
//     const percentageText = document.getElementById('percentageText');
//     let progress = 0;
//
//     // غیرفعال کردن اسکرول و کلیک
//     document.body.style.overflow = 'hidden';
//
//     // شبیه‌سازی پیشرفت واقعی
//     // const simulateProgress = () => {
//     //     const resources = performance.getEntriesByType('resource');
//     //     const total = resources.length;
//     //     const loaded = resources.filter(r => r.duration > 0).length;
//     //     const realProgress = Math.min((loaded / total) * 100, 100);
//     //
//     //     // به‌روزرسانی پیشرفت
//     //     progress = Math.min(progress + 2, realProgress);
//     //     progressBar.style.width = progress + '%';
//     //     percentageText.textContent = Math.round(progress) + '%';
//     //
//     //     if(progress < 100) {
//     //         requestAnimationFrame(simulateProgress);
//     //     }
//     // };
//
//     // شروع فرآیند
//     // simulateProgress();
//
//     // پایان بارگذاری
//     // window.addEventListener('load', () => {
//     //     // تکمیل نوار پیشرفت
//     //     progressBar.style.width = '100%';
//     //     percentageText.textContent = '100%';
//     //
//     //     // محو شدن پس از 500ms
//     //     setTimeout(() => {
//     //         loadingOverlay.style.opacity = '0';
//     //         setTimeout(() => {
//     //             loadingOverlay.remove();
//     //             document.body.style.overflow = 'auto';
//     //         }, 500);
//     //     }, 500);
//     // });
// });
// document.addEventListener('DOMContentLoaded', function() {
//   const loadingOverlay = document.createElement('div');
//   loadingOverlay.id = 'loadingOverlay';
//   loadingOverlay.style.position = 'fixed';
//   loadingOverlay.style.top = '0';
//   loadingOverlay.style.left = '0';
//   loadingOverlay.style.width = '100%';
//   loadingOverlay.style.height = '100%';
//   loadingOverlay.style.backgroundColor = 'rgba(255, 255, 255, 0.9)';
//   loadingOverlay.style.display = 'flex';
//   loadingOverlay.style.justifyContent = 'center';
//   loadingOverlay.style.alignItems = 'center';
//   loadingOverlay.style.zIndex = '9999';
//   document.body.appendChild(loadingOverlay);
//
//   const progressBarContainer = document.createElement('div');
//   progressBarContainer.style.width = '80%';
//   progressBarContainer.style.maxWidth = '400px';
//   progressBarContainer.style.backgroundColor = '#ccc';
//   progressBarContainer.style.borderRadius = '10px';
//   progressBarContainer.style.overflow = 'hidden';
//   loadingOverlay.appendChild(progressBarContainer);
//
//   const progressBar = document.createElement('div');
//   progressBar.style.height = '20px';
//   progressBar.style.width = '0%';
//   progressBar.style.backgroundColor = '#4caf50';
//   progressBarContainer.appendChild(progressBar);
//
//   const percentageText = document.createElement('span');
//   percentageText.style.position = 'absolute';
//   percentageText.style.fontSize = '16px';
//   percentageText.style.color = '#000';
//   percentageText.style.marginTop = '30px';
//   loadingOverlay.appendChild(percentageText);
//
//   document.body.style.overflow = 'hidden';
//
//   const images = document.images;
//   const totalImages = images.length;
//   let loadedImages = 0;
//
//   if (totalImages === 0) {
//     completeLoading();
//   } else {
//     for (let i = 0; i < totalImages; i++) {
//       let img = images[i];
//       if (img.complete) {
//         incrementProgress();
//       } else {
//         img.addEventListener('load', incrementProgress, false);
//         img.addEventListener('error', incrementProgress, false);
//       }
//     }
//   }
//
//   function incrementProgress() {
//     loadedImages++;
//     const progress = Math.round((loadedImages / totalImages) * 100);
//     progressBar.style.width = progress + '%';
//     percentageText.textContent = progress + '%';
//     if (loadedImages >= totalImages) {
//       completeLoading();
//     }
//   }
//
//   function completeLoading() {
//     progressBar.style.width = '100%';
//     percentageText.textContent = '100%';
//     setTimeout(() => {
//       loadingOverlay.style.opacity = '0';
//       setTimeout(() => {
//         document.body.removeChild(loadingOverlay);
//         document.body.style.overflow = 'auto';
//       }, 500);
//     }, 500);
//   }
// });


// document.addEventListener('DOMContentLoaded', function() {
//     const loadingOverlay = document.getElementById('loadingOverlay');
//     const progressBar = document.getElementById('progressBar');
//     const percentageText = document.getElementById('percentageText');
//     let loadedImages = 0;
//
//     document.body.style.overflow = 'hidden';
//
//     const images = document.querySelectorAll('img');
//     const totalImages = images.length;
//
//     if(totalImages === 0) {
//         completeProgress();
//         return;
//     }
//
//     const updateProgress = () => {
//         loadedImages++;
//         // محاسبه پیشرفت واقعی
//         const realProgress = Math.round((loadedImages / totalImages) * 100);
//
//         // نمایش پیشرفت مصنوعی (دو برابر پیشرفت واقعی)
//         const fakeProgress = Math.min(realProgress * 2, 100);
//
//         progressBar.style.width = fakeProgress + '%';
//         percentageText.textContent = fakeProgress + '%';
//
//         if(realProgress >= 50) { // وقتی 50% واقعی رسید
//             completeProgress();
//         }
//     };
//
//     images.forEach(img => {
//         if(img.complete) {
//             updateProgress();
//         } else {
//             img.addEventListener('load', updateProgress);
//             img.addEventListener('error', updateProgress);
//         }
//     });
//
//     function completeProgress() {
//         // حذف تمام لیستنرها برای جلوگیری از آپدیتهای بعدی
//         images.forEach(img => {
//             img.removeEventListener('load', updateProgress);
//             img.removeEventListener('error', updateProgress);
//         });
//
//         // فورس کردن نمایش 100%
//         progressBar.style.width = '100%';
//         percentageText.textContent = '100%';
//
//         setTimeout(() => {
//             loadingOverlay.style.opacity = '0';
//             setTimeout(() => {
//                 loadingOverlay.remove();
//                 document.body.style.overflow = 'auto';
//             }, 500);
//         }, 500);
//     }
//
//     // فالس استارت برای مواردی که بارگذاری طول می‌کشد
//     setTimeout(completeProgress, 5000); // حداکثر 5 ثانیه
// });


document.addEventListener('DOMContentLoaded', function() {
    const loadingOverlay = document.getElementById('loadingOverlay');
    const progressBar = document.getElementById('progressBar');
    const percentageText = document.getElementById('percentageText');
    let loadedImages = 0;

    document.body.style.overflow = 'hidden';

    const images = document.querySelectorAll('img');
    const totalImages = images.length;

    if(totalImages === 0) {
        completeProgress();
        return;
    }

    const updateProgress = () => {
        loadedImages++;
        // محاسبه پیشرفت واقعی
        const realProgress = Math.round((loadedImages / totalImages) * 100);

        // نمایش پیشرفت مصنوعی (دو برابر پیشرفت واقعی)
        const fakeProgress = Math.min(realProgress * 2, 100);

        progressBar.style.width = fakeProgress + '%';
        percentageText.textContent = fakeProgress + '%';

        if(realProgress >= 50) { // وقتی 50% واقعی رسید
            completeProgress();
        }
    };

    images.forEach(img => {
        if(img.complete) {
            updateProgress();
        } else {
            img.addEventListener('load', updateProgress);
            img.addEventListener('error', updateProgress);
        }
    });

    function completeProgress() {
        // حذف تمام لیستنرها برای جلوگیری از آپدیتهای بعدی
        images.forEach(img => {
            img.removeEventListener('load', updateProgress);
            img.removeEventListener('error', updateProgress);
        });

        // فورس کردن نمایش 100%
        progressBar.style.width = '100%';
        percentageText.textContent = '100%';

        setTimeout(() => {
            loadingOverlay.style.opacity = '0';
            setTimeout(() => {
                loadingOverlay.remove();
                document.body.style.overflow = 'auto';
            }, 500);
        }, 500);
    }

    // فالس استارت برای مواردی که بارگذاری طول می‌کشد
    setTimeout(completeProgress, 5000); // حداکثر 5 ثانیه
});


// در فایل new_home.js
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.quick_item.disabled').forEach(item => {
    item.addEventListener('click', e => {
      if (!isLoggedIn) {
        e.preventDefault();
        M.toast({html: 'لطفاً ابتدا وارد حساب کاربری خود شوید', classes: 'rounded'});
      }
    });
  });
});