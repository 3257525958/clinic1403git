document.addEventListener('DOMContentLoaded', function() {
    // مدیریت مودال پرداخت بیعانه
    const modal = document.getElementById('deposit-modal');
    const openBtn = document.getElementById('open-deposit-modal');
    const closeBtn = document.querySelector('.close');

    openBtn.addEventListener('click', () => {
        modal.style.display = 'block';
    });

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    // تبدیل مبلغ به تومان و حروف
    const amountInput = document.getElementById('deposit-amount');
    const tomanDisplay = document.getElementById('toman-amount');
    const wordsDisplay = document.getElementById('words-amount');

    amountInput.addEventListener('input', function() {
        const amount = parseInt(this.value) || 0;
        const toman = Math.floor(amount / 10); // ریال به تومان
        tomanDisplay.textContent = toman.toLocaleString('fa-IR') + ' تومان';
        wordsDisplay.textContent = convertToWords(toman) + ' تومان';
    });

// جایگزین کردن تابع convertToWords با این نسخه کامل
function convertToWords(num) {
    if (num === 0) return 'صفر';

    const units = ['', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه'];
    const teens = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده'];
    const tens = ['', '', 'بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود'];
    const hundreds = ['', 'صد', 'دویست', 'سیصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد'];
    const scales = ['', 'هزار', 'میلیون', 'میلیارد'];

    function convertChunk(chunk) {
        const str = chunk.toString().padStart(3, '0');
        const h = parseInt(str[0]);
        const t = parseInt(str[1]);
        const u = parseInt(str[2]);
        let parts = [];

        if (h > 0) {
            parts.push(hundreds[h]);
        }

        if (t === 1) {
            parts.push(teens[u]);
        } else {
            if (t > 1) {
                parts.push(tens[t]);
            }
            if (u > 0) {
                parts.push(units[u]);
            }
        }

        return parts.join(' و ');
    }

    const numStr = num.toString();
    const chunks = [];
    for (let i = numStr.length; i > 0; i -= 3) {
        chunks.push(numStr.substring(Math.max(0, i-3), i));
    }

    let words = [];
    for (let i = 0; i < chunks.length; i++) {
        const chunk = parseInt(chunks[i]);
        if (chunk > 0) {
            words.push(convertChunk(chunk) + (scales[i] ? ' ' + scales[i] : ''));
        }
    }

    return words.reverse().join(' و ');
}

// در قسمت event listener مقدار تومان را محاسبه کنیم
amountInput.addEventListener('input', function() {
    const amount = parseInt(this.value) || 0;
    const toman = Math.floor(amount / 10); // تبدیل ریال به تومان
    tomanDisplay.textContent = toman.toLocaleString('fa-IR') + ' تومان';
    wordsDisplay.textContent = convertToWords(toman) + ' تومان';
});
    // ثبت بیعانه
    const submitDepositBtn = document.getElementById('submit-deposit');
    submitDepositBtn.addEventListener('click', function() {
        const amount = amountInput.value;
        const bankId = document.getElementById('bank-select').value;
        const tomanword = wordsDisplay.textContent;
        // if (!amount || amount < 100000) {
        //     alert('لطفاً مبلغ بیعانه را وارد کنید (حداقل 100,000 ریال)');
        //     return;
        // }

        fetch(window.APP_CONFIG.SAVE_RESERV_PROFILES_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                action: 'deposit',
                amount: amount,
                bank_id: bankId,
                tomanword : tomanword,
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('بیعانه با موفقیت ثبت شد!');
                location.reload(); // رفرش صفحه برای نمایش اطلاعات جدید
            } else {
                alert('خطا: ' + data.error);
            }
        });
    });

    // ثبت نهایی رزرو
    const submitReservationBtn = document.getElementById('submit-reservation');
    submitReservationBtn.addEventListener('click', function() {
        fetch(window.APP_CONFIG.SAVE_RESERV_PROFILES_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                action: 'finalize'
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('رزرو با موفقیت ثبت شد!');
                window.location.href = '/'; // بازگشت به صفحه اصلی
            } else {
                alert('خطا: ' + data.error);
            }
        });
    });


    // تابع دریافت کوکی CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});