// app.js
document.addEventListener('DOMContentLoaded', function() {
    // مدیریت کارت‌های خدمات
    document.querySelectorAll('.service-card').forEach(function(card) {
        var header = card.querySelector('.card-header');
        header.addEventListener('click', function(e) {
            e.stopPropagation();
            var isActive = card.classList.contains('active');

            // بستن تمام کارت‌های دیگر
            document.querySelectorAll('.service-card').forEach(function(otherCard) {
                otherCard.classList.remove('active');
            });

            // تغییر وضعیت کارت فعلی
            if (!isActive) {
                card.classList.add('active');
                setTimeout(function() {
                    card.scrollIntoView({behavior: 'smooth', block: 'nearest'});
                }, 300);
            }
        });
    });

    // مدیریت تقویم
    moment.loadPersian({ usePersianDigits: true });

    var calendarContainer = document.getElementById('calendarContainer');
    var timeGrid = document.getElementById('timeGrid');
    var timeDayLabel = document.getElementById('timeDayLabel');
    var startDate = moment().add(2, 'days').startOf('day');
    var daysToShow = 30;

    function generateCalendar() {
        calendarContainer.innerHTML = '';
        for (var i = 0; i < daysToShow; i++) {
            var day = startDate.clone().add(i, 'days');
            var dayCell = document.createElement('div');
            dayCell.className = 'day-cell';

            // ایجاد محتوا با روش امن
            dayCell.innerHTML = [
                day.format('dddd'),
                '<br>',
                day.format('jYYYY/jMM/jDD')
            ].join('');

            dayCell.addEventListener('click', function() {
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

        // منطق فعال/غیرفعال
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

    // اجرای اولیه
    generateCalendar();
    document.querySelector('.day-cell').click();
});