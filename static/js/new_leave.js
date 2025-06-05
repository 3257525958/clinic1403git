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
      const a =moment().add(dayIndex+1,'days').startOf('day').format('jYYYY/jMM/jDD')
      const b =moment().add(dayIndex+1,'days').startOf('day').format('dddd')
      timeDayLabel.innerText = 'تایم‌های روز ' + b + a;

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
    const slotsCount = 40;

    for (let i = 0; i < slotsCount; i++) {
        const slotTime = baseTime.clone().add(i * 15, 'minutes');
        const timeStr = slotTime.format('H:mm');
        const timeSlot = document.createElement('div');
        timeSlot.className = 'time-slot';
        timeSlot.dataset.timeIndex = i; // ذخیره اندیس تایم
        timeSlot.innerText = "ساعت " + toPersianNumbers(timeStr);

        // بررسی وضعیت تایم (رزرو شده یا آزاد)
        const isReserved = window.reservedTimes && window.reservedTimes.includes(i);
        const isReservedByOthers = window.rar && window.rar.includes(i);

        if (isReserved) {
            timeSlot.classList.add('reserved');
        } else if (isReservedByOthers) {
            timeSlot.classList.add('reserved-by-others');
            timeSlot.classList.add('disabled');
        } else {
            timeSlot.classList.add('available');
        }


        if (isReserved) {
            timeSlot.classList.add('reserved');
        } else if (isReservedByOthers) {
            timeSlot.classList.add('reserved-by-others');
            timeSlot.classList.add('disabled');
        } else {
            timeSlot.classList.add('available');
        }

        // فقط برای تایم‌های قابل تغییر (غیر رزرو شده توسط دیگران) event listener اضافه می‌کنیم
        if (!isReservedByOthers) {
            timeSlot.addEventListener('click', async () => {
                const dayIndex = Math.floor(date.diff(startDate, 'days')) + 1;
                const slotIndex = i + 1; // تبدیل به اندیس 1-40

                // دریافت وضعیت فعلی
                const wasReserved = timeSlot.classList.contains('reserved');

                // ارسال درخواست به سرور
                const success = await sendTimeToBackend(dayIndex, slotIndex);

                if (success) {
                    // تغییر وضعیت UI
                    timeSlot.classList.toggle('reserved', !wasReserved);
                    timeSlot.classList.toggle('available', wasReserved);

                    // به‌روزرسانی لیست reservedTimes
                    if (wasReserved) {
                        const index = window.reservedTimes.indexOf(i);
                        if (index !== -1) window.reservedTimes.splice(index, 1);
                    } else {
                        if (!window.reservedTimes) window.reservedTimes = [];
                        window.reservedTimes.push(i);
                    }
                }
            });
        }

        timeGrid.appendChild(timeSlot);
    }
}
function sendDateToBackend(dayIndex) {
  const nationalcode = document.getElementById('nationalcode').value;
  console.log("Sending day index:", dayIndex);
  fetch('/reserv/new_timeleave/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    credentials: 'same-origin',  // اطمینان از ارسال کوکی‌ها (session) به سرور
    body: JSON.stringify({ selected_date: dayIndex , nationalcode: nationalcode})
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
      window.rar = data.rar;
      console.log('Updated Reserved Times:', window.rar);
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
async function sendTimeToBackend(dayIndex, timeNumber) {
    const nationalcode = document.getElementById('nationalcode').value;

    try {
        // پیدا کردن عنصر مربوطه
        const timeSlotElement = document.querySelector('.time-slot[data-time-index="${timeNumber - 1}"]');
        let originalText = '';

        if (timeSlotElement) {
            originalText = timeSlotElement.innerText;
            timeSlotElement.innerText = 'در حال پردازش...';
        }

        // ارسال درخواست
        const response = await fetch('/reserv/new_timeleave/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            credentials: 'same-origin',
            body: JSON.stringify({
                day: dayIndex,
                time: timeNumber,
                nationalcode: nationalcode
            })
        });

        // بازگردانی متن اصلی
        if (timeSlotElement) {
            timeSlotElement.innerText = originalText;
        }

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error("خطای سرور: ${response.status} - ${errorText}");
        }

        const data = await response.json();

        // بررسی وجود خطا در پاسخ سرور
        if (data.error) {
            throw new Error(data.error);
        }

        // به‌روزرسانی لیست reservedTimes با داده‌های جدید از سرور
        if (data.reserved_times) {
            window.reservedTimes = data.reserved_times;
            return true;
        }

        throw new Error('پاسخ سرور نامعتبر است');

    } catch (error) {
        console.error('خطا در ارتباط با سرور:', error);
        alert('خطا: ${error.message}');
        return false;
    }
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
// اجرای اولیه: تولید تقویم، پیش‌انتخاب اولین روز و تولید تایم‌های آن
generateCalendar();
selectedDate = startDate.clone();
const firstCell = calendarContainer.querySelector('.day-cell');
if (firstCell) {
    firstCell.classList.add('selected');
    firstCell.click(); // فعال‌سازی کلیک خودکار روی روز اول
}
      const aa =moment().add(2,'days').startOf('day').format('jYYYY/jMM/jDD')
      const bb =moment().add(2,'days').startOf('day').format('dddd')

timeDayLabel.innerText = 'تایم‌های روز ' + bb + aa;  // اولین خانه برابر 1 است
sendDateToBackend(1);
// generateTimeSlots(startDate);
// مدیریت دکمه‌ها
document.getElementById('confirmBtn').addEventListener('click', () => {
    if (confirm('آیا از ثبت مرخصی‌ها اطمینان دارید؟')) {
        alert('مرخصی با موفقیت ثبت شد!');
        // ارسال درخواست نهایی به سرور
        fetch('/reserv/finalize_leave/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        }).then(() => {
            window.location.href = '/';
        });
    }
});

document.getElementById('cancelBtn').addEventListener('click', () => {
    if (confirm('آیا مایل به لغو تغییرات هستید؟')) {
        window.history.back();
    }
});