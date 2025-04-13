// فعال‌سازی حالت شمسی با ارقام فارسی
moment.loadPersian({ usePersianDigits: true });

const calendarContainer = document.getElementById('calendarContainer');
const timeGrid = document.getElementById('timeGrid');
const timeDayLabel = document.getElementById('timeDayLabel');

let selectedDate = null;
let datetime = 0; // متغیر ذخیره شماره تایم انتخاب‌شده (مثلاً 1 برای اولین تایم)

// تاریخ شروع: دو روز بعد از امروز (امروز و فردا غیرقابل انتخاب)
const startDate = moment().add(2, 'days').startOf('day');
const daysToShow = 30;

// تولید تقویم روزها
function generateCalendar() {
  calendarContainer.innerHTML = '';
  for (let i = 0; i < daysToShow; i++) {
    const day = startDate.clone().add(i, 'days');
    const dayCell = document.createElement('div');
    dayCell.className = 'day-cell';
    dayCell.innerHTML = `
      <div class="day-week">${day.format('dddd')}</div>
      <div class="day-date">${day.format('jYYYY/jMM/jDD')}</div>
    `;
    // اضافه کردن مقدار ایندکس به عنوان data attribute (اختیاری)
    dayCell.dataset.dayIndex = i + 1;

    dayCell.addEventListener('click', () => {
      // حذف انتخاب از تمام سلول‌ها و انتخاب سلول فعلی
      document.querySelectorAll('.day-cell').forEach(cell => cell.classList.remove('selected'));
      dayCell.classList.add('selected');

      selectedDate = day;
      const dayIndex = i + 1; // اگر خانه دوم کلیک شود، dayIndex برابر با 2 خواهد بود

      // به‌روزرسانی برچسب تایم روز با شماره روز (مثلاً "تایم‌های روز 2")
      timeDayLabel.innerText = 'تایم‌های روز ' + dayIndex;

      // ارسال شماره روز به سرور به جای تاریخ کامل
      sendDateToBackend(dayIndex);

      // تولید مجدد سلول‌های تایم با تاریخ انتخاب‌شده
      generateTimeSlots(day);
    });
    calendarContainer.appendChild(dayCell);
  }
}

// تولید تایم‌ها برای روز انتخاب‌شده
function generateTimeSlots(date) {
  timeGrid.innerHTML = '';
  const baseTime = moment(date.format('YYYY-MM-DD') + ' 10:00', 'YYYY-MM-DD HH:mm');
  const slotsCount = 40; // از ساعت ۱۰:۰۰ تا ۲۰:۰۰ با فاصله ۱۵ دقیقه

  for (let i = 0; i < slotsCount; i++) {
    const slotTime = baseTime.clone().add(i * 15, 'minutes');
    const timeStr = slotTime.format(1+'H:mm');
    const timeSlot = document.createElement('div');
    timeSlot.className = 'time-slot';
    timeSlot.innerText = "ساعت " + toPersianNumbers(timeStr);

    // بررسی اینکه آیا این اندیس در آرایه window.reservedTimes قرار دارد یا خیر
    if (window.reservedTimes && window.reservedTimes.includes(i)) {
      timeSlot.classList.add('disabled');
    } else {
      timeSlot.addEventListener('click', () => {
        // حذف کلاس active از تمامی تایم‌ها و افزودن به تایم انتخاب‌شده
        document.querySelectorAll('.time-slot').forEach(slot => slot.classList.remove('active'));
        timeSlot.classList.add('active');
        const slotIndex = i + 1; // شماره تایم (اندیس + 1)
        sendTimeToBackend(dayIndex, slotIndex);
      });
    }
    timeGrid.appendChild(timeSlot);
  }
}

// ارسال شماره روز به سرور با متد POST
function sendDateToBackend(dayIndex) {
  console.log("Sending day index:", dayIndex);
  fetch('/reserv/new_timereserv/', {
  // fetch('http://drmahdiasadpour.ir/reserv/new_timereserv/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    credentials: 'same-origin',  // اطمینان از ارسال کوکی‌ها (session) به سرور
    body: JSON.stringify({ selected_date: dayIndex })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Bad Request: " + response.status);
    }
    return response.json();
  })
  .then(data => {
    if (data.reserved_times) {
      window.reservedTimes = data.reserved_times;
      console.log('Updated Reserved Times:', window.reservedTimes);
      // به‌روزرسانی مجدد تایم‌ها با تاریخ انتخاب‌شده
      if (selectedDate) {
        generateTimeSlots(selectedDate);
      }
    } else {
      console.error('No reserved_times returned from server');
    }
  })
  .catch(error => console.error('Error in sending date:', error));
}

// ارسال شماره تایم به همراه شماره روز به سرور با متد POST
function sendTimeToBackend(dayIndex, timeNumber) {
  fetch('http://localhost:8000/reserv/new_timereserv/', {
  // fetch('http://drmahdiasadpour.ir/reserv/new_timereserv/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({ dateday: dayIndex, datetime: timeNumber })
  })
  .then(response => {
    if (response.ok) {
      console.log('تایم ارسال شد:', dayIndex, timeNumber);
    } else {
      console.error('خطا در ارسال تایم');
    }
  })
  .catch(error => console.error('خطا:', error));
}

// تبدیل اعداد انگلیسی به فارسی
function toPersianNumbers(str) {
  const persianDigits = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹'];
  return str.toString().replace(/\d/g, d => persianDigits[d]);
}

// تابع کمکی برای دریافت CSRF Token از کوکی‌ها
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// اجرای اولیه: تولید تقویم، پیش‌انتخاب اولین روز و تولید تایم‌های آن
generateCalendar();
selectedDate = startDate.clone();
const firstCell = calendarContainer.querySelector('.day-cell');
if (firstCell) {
  firstCell.classList.add('selected');
}
timeDayLabel.innerText = 'تایم‌های روز ' + 1;  // اولین خانه برابر 1 است
sendDateToBackend(1);
generateTimeSlots(startDate);