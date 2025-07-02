document.addEventListener('DOMContentLoaded', function() {
  // عناصر DOM
  const depositModal = document.getElementById('deposit-modal');
  const openModalBtn = document.getElementById('open-deposit-modal');
  const closeModal = document.querySelector('.close');
  const depositAmount = document.getElementById('deposit-amount');
  const tomanAmount = document.getElementById('toman-amount');
  const wordsAmount = document.getElementById('words-amount');
  const submitDeposit = document.getElementById('submit-deposit');

  // باز کردن مودال
  openModalBtn.addEventListener('click', function() {
    depositModal.style.display = 'block';
  });

  // بستن مودال
  closeModal.addEventListener('click', function() {
    depositModal.style.display = 'none';
  });

  // بستن مودال با کلیک خارج از آن
  window.addEventListener('click', function(event) {
    if (event.target === depositModal) {
      depositModal.style.display = 'none';
    }
  });

  // تبدیل مبلغ و نمایش
  depositAmount.addEventListener('input', function() {
    const amount = parseInt(this.value) || 0;
    const toman = Math.floor(amount / 10);

    tomanAmount.textContent = toman.toLocaleString('fa-IR') + ' تومان';
    wordsAmount.textContent = convertToWords(toman) + ' تومان';
  });

  // ثبت پرداخت
  submitDeposit.addEventListener('click', function(event) {
    event.preventDefault(); // جلوگیری از رفتار پیشفرض

    const amount = parseInt(depositAmount.value);
    const bankId = document.getElementById('bank-select').value;

    if (!amount || amount < 100000) {
      alert('لطفاً مبلغ بیعانه را وارد کنید (حداقل 100,000 ریال)');
      return;
    }

    // ارسال درخواست به سرور
    const url = '{% url "save_reserv_profiles" %}';
    const csrfToken = getCookie('csrftoken');

    fetch(url, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        deposit_amount: amount,
        bank_id: bankId
      })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('پاسخ شبکه نامعتبر بود');
      }
      return response.json();
    })
    .then(data => {
      if (data.status === 'success') {
        alert('پرداخت بیعانه با موفقیت ثبت شد!');
        depositModal.style.display = 'none';

        // ریدایرکت به صفحه بعدی (اختیاری)
        if (data.redirect_url) {
          window.location.href = data.redirect_url;
        }
      } else {
        alert('خطا: ' + data.message);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('خطا در ارتباط با سرور: ' + error.message);
    });
  });

  // تابع تبدیل عدد به حروف فارسی (تا 999,999,999)
  function convertToWords(number) {
    if (number === 0) return 'صفر';

    const units = ['', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه'];
    const teens = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده'];
    const tens = ['', '', 'بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود'];
    const hundreds = ['', 'صد', 'دویست', 'سیصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد'];
    const scales = ['', 'هزار', 'میلیون', 'میلیارد'];

    function convertChunk(chunk) {
      const num = parseInt(chunk);
      if (num === 0) return '';

      const h = Math.floor(num / 100);
      const t = Math.floor((num % 100) / 10);
      const u = num % 10;

      let words = [];

      if (h > 0) words.push(hundreds[h]);

      if (t === 1) {
        words.push(teens[u]);
      } else {
        if (t > 1) words.push(tens[t]);
        if (u > 0) words.push(units[u]);
      }

      return words.join(' و ');
    }

    const numStr = number.toString();
    const chunks = [];

    for (let i = numStr.length; i > 0; i -= 3) {
      chunks.push(numStr.substring(Math.max(0, i - 3), i));
    }

    let result = [];
    for (let i = 0; i < chunks.length; i++) {
      const chunk = parseInt(chunks[i]);
      if (chunk > 0) {
        result.unshift(convertChunk(chunks[i]) + ' ' + scales[i]);
      }
    }

    return result.join(' و ').trim();
  }

  // تابع برای دریافت مقدار کوکی
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
