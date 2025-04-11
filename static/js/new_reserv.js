document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded");

    // مدیریت باز و بسته شدن کارت‌های خدمات
    document.querySelectorAll('.service-card').forEach(function(card) {
        var header = card.querySelector('.card-header');
        if (!header) {
            console.error("هیچ المان .card-header در کارت یافت نشد", card);
            return;
        }
        header.addEventListener('click', function(e) {
            e.stopPropagation();
            console.log("Card header clicked");
            console.log("کلاس‌های کارت قبل از تغییر:", card.classList);

            var isActive = card.classList.contains('active');

            // بستن تمام کارت‌های دیگر
            document.querySelectorAll('.service-card').forEach(function(otherCard) {
                otherCard.classList.remove('active');
                var optCont = otherCard.querySelector('.options-container');
                if (optCont) {
                    // تنظیم مستقیم max-height به صفر برای بستن لیست
                    optCont.style.maxHeight = "0px";
                }
            });

            // تغییر وضعیت کارت فعلی
            if (!isActive) {
                card.classList.add('active');
                var optionsContainer = card.querySelector('.options-container');
                if (optionsContainer) {
                    // تنظیم max-height به صورت مستقیم بر اساس ارتفاع محتوا
                    optionsContainer.style.maxHeight = optionsContainer.scrollHeight + "px";
                }
                console.log("کلاس‌های کارت بعد از تغییر:", card.classList);
                setTimeout(function() {
                    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 300);
            }
        });
    });

    // اجرای تقویم در صورت وجود moment.js
    if (typeof moment !== 'undefined') {
        moment.loadPersian({ usePersianDigits: true });
        var calendarContainer = document.getElementById('calendarContainer');
        var timeGrid = document.getElementById('timeGrid');
        var startDate = moment().add(2, 'days').startOf('day');
        var daysToShow = 30;

        function generateCalendar() {
            if (!calendarContainer) return;
            calendarContainer.innerHTML = '';
            for (var i = 0; i < daysToShow; i++) {
                var day = startDate.clone().add(i, 'days');
                var dayCell = document.createElement('div');
                dayCell.className = 'day-cell';
                dayCell.innerHTML = [
                    day.format('dddd'),
                    '<br>',
                    day.format('jYYYY/jMM/jDD')
                ].join('');
                dayCell.addEventListener('click', function() {
                    console.log("روز کلیک شد:", this.innerText);
                    handleDayClick(this, day);
                });
                calendarContainer.appendChild(dayCell);
            }
        }

        function handleDayClick(cell, day) {
            document.querySelectorAll('.day-cell').forEach(function(c) {
                c.classList.remove('selected');
            });
            cell.classList.add('selected');
            updateTimeSlots(day);
        }

        function updateTimeSlots(day) {
            if (!timeGrid) return;
            timeGrid.innerHTML = '';
            var baseTime = day.clone().hour(10).minute(0);
            for (var i = 0; i < 40; i++) {
                var slotTime = baseTime.clone().add(i * 15, 'minutes');
                var timeSlot = createTimeSlot(slotTime, i, day);
                timeGrid.appendChild(timeSlot);
            }
        }

        function createTimeSlot(time, index, day) {
            var slot = document.createElement('div');
            slot.className = 'time-slot';
            slot.textContent = 'ساعت ' + toPersianNumbers(time.format('HH:mm'));
            // منطق فعال/غیرفعال کردن اسلات‌های زمانی
            var isDisabled = day.isSame(startDate, 'day') && (index === 2 || index === 3);
            if (isDisabled) {
                slot.classList.add('disabled');
            } else {
                slot.addEventListener('click', function() {
                    handleTimeClick(this, index);
                });
            }
            return slot;
        }

        function handleTimeClick(slot, index) {
            document.querySelectorAll('.time-slot').forEach(function(s) {
                s.classList.remove('active');
            });
            slot.classList.add('active');
            console.log('زمان انتخاب شده:', index + 1);
        }

        function toPersianNumbers(str) {
            return str.toString().replace(/\d/g, function(d) {
                return ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹'][d];
            });
        }

        generateCalendar();
        if (document.querySelector('.day-cell')) {
            document.querySelector('.day-cell').click();
        }
    } else {
        console.warn("کتابخانه moment.js بارگذاری نشده است؛ کد تقویم اجرا نخواهد شد.");
    }

    // ارسال مشخصات انتخاب شده به بکند با متد POST
    document.querySelectorAll('.option-item').forEach(function(item) {
        item.addEventListener('click', function(e) {
            e.stopPropagation();
            console.log("روی گزینه کلیک شد");

            const service = this.getAttribute('data-service-id');
            const option = this.getAttribute('data-option-id');
            const nationalcode = document.getElementById('nationalcode').value;
            console.log("Service:", service, "Option:", option);

            if (!service || !option) {
                console.error("اطلاعات داده‌ای مورد نیاز یافت نشد");
                return;
            }

            // fetch('http://localhost:8000/reserv/save_selection/', {
            fetch('http://drmahdiasadpour.ir/reserv/save_selection/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ service: service, option: option ,nationalcode: nationalcode})
            })
            .then(response => {
                console.log("وضعیت پاسخ:", response.status);
                return response.json();
            })
            .then(data => {
                console.log('اطلاعات ارسال شد:', data);
                if (data.redirect_url) {
                    window.location.href = data.redirect_url; // انتقال به صفحه جدید
                }
            })
            .catch(error => {
                console.error('خطا در ارسال اطلاعات:', error);
            });
        });
    });

    // تابع کمکی برای دریافت CSRF Token از کوکی‌ها (در صورت استفاده از Django)
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
});

