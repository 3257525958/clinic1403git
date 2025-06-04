document.addEventListener('DOMContentLoaded', function () {
  // فعال‌سازی تقویم شمسی
  $("#birthdate").persianDatepicker({
    observer: true,
    format: 'YYYY/MM/DD',
    autoClose: true,
    initialValue: false,
    onSelect: function (unix) {
      let date = new persianDate(unix);
      let formattedDate = date.format("YYYY/MM/DD");
      document.getElementById('birthdate').value = formattedDate;
    }
  });

  // نمایش تقویم هنگام کلیک روی آیکون
  document.getElementById('calendar-icon').addEventListener('click', function () {
    $("#birthdate").persianDatepicker('show');
  });

  // اعتبارسنجی شماره تلفن
  document.querySelector('.edit-form').addEventListener('submit', function (e) {
    const phone = document.getElementById('phone').value;
    if (!/^09\d{9}$/.test(phone)) {
      e.preventDefault();
      Swal.fire({
        icon: 'error',
        title: 'شماره موبایل نامعتبر',
        text: 'لطفاً شماره موبایل را به صورت صحیح وارد کنید (09xxxxxxxxx)'
      });
    }
  });

  // نمایش پیش‌نمایش تصویر انتخاب شده
  const fileInput = document.getElementById('profile_picture');
  const fileText = document.querySelector('.file-text');

  fileInput.addEventListener('change', function() {
    if (this.files && this.files[0]) {
      fileText.textContent = this.files[0].name;

      // نمایش پیش‌نمایش تصویر
      const reader = new FileReader();
      reader.onload = function(e) {
        document.querySelector('.current-profile img').src = e.target.result;
      }
      reader.readAsDataURL(this.files[0]);
    }
  });
});