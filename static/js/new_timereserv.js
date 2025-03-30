    // فعال‌سازی حالت شمسی با ارقام فارسی
    moment.loadPersian({ usePersianDigits: true });

    const calendarContainer = document.getElementById('calendarContainer');
    const timeGrid = document.getElementById('timeGrid');
    const timeDayLabel = document.getElementById('timeDayLabel');

    let selectedDate = null;
    let dateday = "";    // متغیر ذخیره تاریخ انتخاب‌شده
    let datetime = 0;    // متغیر ذخیره شماره تایم انتخاب‌شده (مثلاً 1 برای اولین تایم)

    // شروع از دو روز بعد (امروز و فردا غیرقابل انتخاب)
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
        dayCell.addEventListener('click', () => {
          document.querySelectorAll('.day-cell').forEach(cell => cell.classList.remove('selected'));
          dayCell.classList.add('selected');
          selectedDate = day;
          dateday = day.format('jYYYY/jMM/jDD');
          // به‌روزرسانی برچسب تایم روز
          timeDayLabel.innerText = 'تایم‌های روز ' + day.format('dddd') + ' ' + dateday;
          sendDateToBackend(dateday);
          generateTimeSlots(day);
        });
        calendarContainer.appendChild(dayCell);
      }
    }

    // تولید تایم‌ها برای روز انتخاب‌شده (با استفاده از حلقه for)
    function generateTimeSlots(date) {
      timeGrid.innerHTML = '';
      const baseTime = moment(date.format('YYYY-MM-DD') + ' 10:00', 'YYYY-MM-DD HH:mm');
      const slotsCount = 40; // از ساعت ۱۰:۰۰ تا ۲۰:۰۰ با فاصله ۱۵ دقیقه
      for (let i = 0; i < slotsCount; i++) {
        const slotTime = baseTime.clone().add(i * 15, 'minutes');
        const timeStr = '۱' + slotTime.format('H:mm');
        const timeSlot = document.createElement('div');
        timeSlot.className = 'time-slot';
        // نمایش زمان به صورت "ساعت ۱۰:۳۰"
        timeSlot.innerText = "ساعت " + toPersianNumbers(timeStr);
        let available = true;
        // اگر روز انتخاب شده همان اولین روز (startDate) باشد، تایم سوم و چهارم (اندیس 2 و 3) غیرقابل انتخاب شوند.
        if (date.isSame(startDate, 'day') && (i === 2 || i === 3)) {
          available = false;
        }
        if (!available) {
          timeSlot.classList.add('disabled');
        } else {
          timeSlot.addEventListener('click', () => {
            document.querySelectorAll('.time-slot').forEach(slot => slot.classList.remove('active'));
            timeSlot.classList.add('active');
            // شماره تایم: اگر روی اولین خانه کلیک شود، عدد 1
            datetime = i + 1;
            sendTimeToBackend(dateday, datetime);
          });
        }
        timeGrid.appendChild(timeSlot);
      }
    }

    // ارسال تاریخ (dateday) به بک‌اند با متد POST
    function sendDateToBackend(formattedDate) {
      fetch('/submitDate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dateday: formattedDate })
      })
      .then(response => {
        if (response.ok) {
          console.log('تاریخ ارسال شد:', formattedDate);
        } else {
          console.error('خطا در ارسال تاریخ');
        }
      })
      .catch(error => console.error('خطا:', error));
    }

    // ارسال شماره تایم (datetime) به همراه تاریخ (dateday) به بک‌اند با متد POST
    function sendTimeToBackend(formattedDate, timeNumber) {
      fetch('/submitTime', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dateday: formattedDate, datetime: timeNumber })
      })
      .then(response => {
        if (response.ok) {
          console.log('تایم ارسال شد:', formattedDate, timeNumber);
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

    // اجرای اولیه: تولید تقویم، پیش‌انتخاب اولین روز و تولید تایم‌های آن
    generateCalendar();
    selectedDate = startDate.clone();
    dateday = startDate.format('jYYYY/jMM/jDD');
    const firstCell = calendarContainer.querySelector('.day-cell');
    if (firstCell) {
      firstCell.classList.add('selected');
    }
    timeDayLabel.innerText = 'تایم‌های روز ' + startDate.format('dddd') + ' ' + dateday;
    sendDateToBackend(dateday);
    generateTimeSlots(startDate);
