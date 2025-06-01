// متغیرهای جهانی
let payments = [];
let totalPayable = 0;
let banks = [];

// تابع تبدیل ریال به تومان
function rialToToman(amount) {
    return Math.floor(amount / 10);
}

// تابع تبدیل عدد به حروف فارسی
function toPersianWords(number) {
    // پیاده‌سازی ساده - در صورت نیاز می‌توانید از کتابخانه‌های خارجی استفاده کنید
    const persianNumbers = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
    return number.toString().replace(/\d/g, digit => persianNumbers[digit]);
}

// تابع فرمت اعداد با جداکننده هزارگان
function formatNumber(number) {
    return new Intl.NumberFormat('fa-IR').format(number);
}

// تابع به‌روزرسانی جمع‌بندی
function updateSummary() {
    // محاسبه مجموع پرداخت‌ها
    const totalPaid = payments.reduce((sum, payment) => sum + payment.amount, 0);

    // به‌روزرسانی نمایش
    document.getElementById('total-paid').textContent = formatNumber(totalPaid);

    // محاسبه مانده قابل پرداخت
    const remaining = totalPayable - totalPaid;
    document.getElementById('remaining-amount').textContent = formatNumber(remaining);

    // فعال/غیرفعال کردن دکمه ثبت
    document.getElementById('submit-payment').disabled = remaining > 0;
}

// تابع نمایش مودال بیعانه
function showAdvanceModal(serviceId, currentAdvance, bankId) {
    const modal = document.getElementById('advance-modal');
    const amountInput = document.getElementById('advance-amount');
    const bankSelect = document.getElementById('advance-bank');
    const wordsDisplay = document.getElementById('advance-toman-words');

    // تنظیم مقادیر اولیه
    document.getElementById('modal-service-id').value = serviceId;
    amountInput.value = currentAdvance;
    bankSelect.value = bankId || banks[0]?.id || '';

    // نمایش مبلغ به تومان
    updateAdvanceWords();

    // نمایش مودال
    modal.style.display = 'block';

    // رویداد تغییر مبلغ
    amountInput.addEventListener('input', updateAdvanceWords);

    function updateAdvanceWords() {
        const amount = parseInt(amountInput.value) || 0;
        const toman = rialToToman(amount);
        wordsDisplay.textContent = toman.toLocaleString('fa-IR') + ' تومان';
    }
}

// تابع ذخیره بیعانه
function saveAdvance() {
    const serviceId = document.getElementById('modal-service-id').value;
    const amount = parseInt(document.getElementById('advance-amount').value) || 0;
    const bankId = document.getElementById('advance-bank').value;

    // ارسال درخواست به سرور
    fetch(updateAdvanceUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            service_id: serviceId,
            advance_amount: amount,
            bank_id: bankId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // به‌روزرسانی نمایش
            const displaySpan = document.getElementById(`advance_display_${serviceId}`);
            displaySpan.textContent = formatNumber(data.new_advance);

            // بستن مودال
            document.getElementById('advance-modal').style.display = 'none';

            // به‌روزرسانی جمع‌بندی
            location.reload();
        } else {
            alert('خطا در ذخیره بیعانه: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('خطا در ارتباط با سرور');
    });
}

// تابع نمایش مودال پرداخت
function showPaymentModal(serviceId, maxAmount) {
    const modal = document.getElementById('payment-modal');
    const amountInput = document.getElementById('payment-amount');
    const wordsDisplay = document.getElementById('payment-toman-words');

    // تنظیم مقادیر اولیه
    document.getElementById('payment-service-id').value = serviceId;
    amountInput.value = '';
    amountInput.max = maxAmount;

    // نمایش مبلغ به تومان
    updatePaymentWords();

    // نمایش مودال
    modal.style.display = 'block';

    // رویداد تغییر مبلغ
    amountInput.addEventListener('input', updatePaymentWords);

    function updatePaymentWords() {
        const amount = parseInt(amountInput.value) || 0;
        const toman = rialToToman(amount);
        wordsDisplay.textContent = toman.toLocaleString('fa-IR') + ' تومان';
    }
}

// تابع افزودن پرداخت
function addPayment() {
    const serviceId = document.getElementById('payment-service-id').value;
    const amount = parseInt(document.getElementById('payment-amount').value) || 0;
    const bankId = document.getElementById('payment-bank').value;

    if (amount <= 0) {
        alert('مبلغ پرداختی باید بیشتر از صفر باشد');
        return;
    }

    // یافتن نام بانک
    const bank = banks.find(b => b.id == bankId);
    const bankName = bank ? bank.onvan : 'نامشخص';

    // یافتن نام خدمت
    const serviceRow = document.querySelector(`[data-service-id="${serviceId}"]`).closest('tr');
    const serviceName = serviceRow.querySelector('td:first-child').textContent;

    // ایجاد رکورد پرداخت
    const payment = {
        id: Date.now(), // شناسه منحصر به فرد
        service_id: serviceId,
        service_name: serviceName,
        amount: amount,
        bank_id: bankId,
        bank_name: bankName
    };

    // افزودن به لیست پرداخت‌ها
    payments.push(payment);

    // افزودن به جدول
    const tableBody = document.querySelector('#payments-table tbody');
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
        <td>${serviceName}</td>
        <td>${formatNumber(amount)}</td>
        <td>${formatNumber(rialToToman(amount))}</td>
        <td>${bankName}</td>
        <td>
            <button class="btn-remove-payment" data-id="${payment.id}">
                حذف
            </button>
        </td>
    `;
    tableBody.appendChild(newRow);

    // اضافه کردن رویداد حذف
    newRow.querySelector('.btn-remove-payment').addEventListener('click', function() {
        const id = parseInt(this.dataset.id);
        payments = payments.filter(p => p.id !== id);
        this.closest('tr').remove();
        updateSummary();
    });

    // بستن مودال
    document.getElementById('payment-modal').style.display = 'none';

    // به‌روزرسانی جمع‌بندی
    updateSummary();
}

// تابع ارسال نهایی
function submitPayment() {
    if (payments.length === 0) {
        alert('هیچ پرداختی ثبت نشده است');
        return;
    }

    // ایجاد فرم برای ارسال
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = submitPaymentUrl;

    // افزودن فیلد CSRF
    const csrfInput = document.createElement('input');
    csrfInput.type = 'hidden';
    csrfInput.name = 'csrfmiddlewaretoken';
    csrfInput.value = csrfToken;
    form.appendChild(csrfInput);

    // افزودن تخفیف‌ها
    document.querySelectorAll('.discount-input').forEach(input => {
        const serviceId = input.id.split('_')[1];
        const discountInput = document.createElement('input');
        discountInput.type = 'hidden';
        discountInput.name = `discount_${serviceId}`;
        discountInput.value = input.value;
        form.appendChild(discountInput);
    });

    // افزودن پرداخت‌ها
    const paymentsInput = document.createElement('input');
    paymentsInput.type = 'hidden';
    paymentsInput.name = 'payments';
    paymentsInput.value = JSON.stringify(payments);
    form.appendChild(paymentsInput);

    // ارسال فرم
    document.body.appendChild(form);
    form.submit();
}// تابع کمکی برای دریافت کوکی
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

// تابع مقداردهی اولیه
function initCashier() {
    // مقداردهی متغیرهای جهانی
    totalPayable = parseInt(document.getElementById('total-payable-amount').dataset.value);
    banks = JSON.parse(document.getElementById('banks-data').textContent);
    document.querySelectorAll('.btn-remove-service').forEach(button => {
        button.addEventListener('click', () => {
            const serviceId = button.dataset.serviceId;
            if (confirm('آیا مطمئنید می‌خواهید این خدمت را از فاکتور حذف کنید؟')) {
                removeService(serviceId);
            }
        });
    });


    // رویدادهای دکمه‌ها
    document.querySelectorAll('.btn-edit-advance').forEach(button => {
        button.addEventListener('click', () => {
            const serviceId = button.dataset.serviceId;
            const currentAdvance = parseInt(button.dataset.currentAdvance) || 0;
            const bankId = button.dataset.bankId || '';
            showAdvanceModal(serviceId, currentAdvance, bankId);
        });
    });

    document.querySelectorAll('.btn-add-payment').forEach(button => {
        button.addEventListener('click', () => {
            const serviceId = button.dataset.serviceId;
            const maxAmount = parseInt(button.dataset.maxAmount);
            showPaymentModal(serviceId, maxAmount);
        });
    });

    document.getElementById('save-advance').addEventListener('click', saveAdvance);
    document.getElementById('add-payment').addEventListener('click', addPayment);
    document.getElementById('submit-payment').addEventListener('click', submitPayment);

    // رویدادهای بستن مودال
    document.querySelectorAll('.close').forEach(button => {
        button.addEventListener('click', () => {
            button.closest('.modal').style.display = 'none';
        });
    });

    // بستن مودال با کلیک خارج از آن
    window.addEventListener('click', (event) => {
        document.querySelectorAll('.modal').forEach(modal => {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });

    // مقداردهی اولیه لیست پرداخت‌ها
    payments = [];
}

// اجرای تابع مقداردهی اولیه پس از بارگذاری صفحه
document.addEventListener('DOMContentLoaded', initCashier);
// تابع حذف سرویس از لیست
function removeService(serviceId) {
    // حذف سطر از جدول
    const row = document.getElementById(`service-row-${serviceId}`);
    if (row) {
        row.remove();

        // حذف از لیست محاسبات
        const serviceIndex = services.findIndex(s => s.id === serviceId);
        if (serviceIndex !== -1) {
            services.splice(serviceIndex, 1);
        }

        // به‌روزرسانی جمع‌بندی
        updateSummary();
    }
}
