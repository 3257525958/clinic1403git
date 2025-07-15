// secretary.js - فایل مدیریت داشبورد منشی
document.addEventListener('DOMContentLoaded', () => {
    // ==================== تنظیمات اولیه ====================
    // عناصر اصلی DOM
    const elements = {
        memberSearch: document.getElementById('memberSearch'),
        searchResults: document.getElementById('searchResults'),
        reservationsList: document.querySelector('.reservations-list'),
        newMemberBtn: document.getElementById('newMemberBtn'),
        closeCashBtn: document.getElementById('closeCashBtn'),
        csrfToken: document.querySelector('[name=csrfmiddlewaretoken]').value
    };

    // بررسی وجود عناصر ضروری
    if (!elements.memberSearch || !elements.searchResults || !elements.reservationsList || !elements.newMemberBtn || !elements.closeCashBtn || !elements.csrfToken) {
        console.error('One or more required elements are missing');
        return;
    }

    // تنظیمات پویا
    const config = {
        minSearchLength: 2,
        debounceTime: 300,
        baseApiUrl: window.location.origin,
        get searchMembersUrl() { return this.baseApiUrl + '/reserv/search_members/'; }
    };

    // وضعیت برنامه
    const state = {
        searchTimeout: null,
        isSearching: false,
        lastQuery: ''
    };

    // ==================== مقداردهی اولیه ====================
    initApplication();

    // ==================== توابع اصلی ====================
    function initApplication() {
        setupEventListeners();
    }

    function setupEventListeners() {
        // جستجوی اعضا با تاخیر (debounce)
        elements.memberSearch.addEventListener('input', handleSearchInput);

        // مدیریت کلیک روی نتایج جستجو
        elements.searchResults.addEventListener('click', handleSearchResultClick);

        // بستن نتایج جستجو هنگام کلیک خارج
        document.addEventListener('click', handleOutsideClick);

        // دکمه‌های عملیاتی
        elements.newMemberBtn.addEventListener('click', () => {
            window.location.href = '/cantact/addreservecantact/';
        });

        elements.closeCashBtn.addEventListener('click', () => {
            window.location.href = '/reserv/close_cash/';
        });
    }

    // تابع تبدیل اعداد فارسی و عربی به لاتین
    function convertDigitsToLatin(input) {
        const persianDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
        const arabicDigits = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩'];
        const latinDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

        let output = input;

        // جایگزینی اعداد فارسی
        persianDigits.forEach((digit, index) => {
            const regex = new RegExp(digit, 'g');
            output = output.replace(regex, latinDigits[index]);
        });

        // جایگزینی اعداد عربی
        arabicDigits.forEach((digit, index) => {
            const regex = new RegExp(digit, 'g');
            output = output.replace(regex, latinDigits[index]);
        });

        return output;
    }

    function handleSearchInput(event) {
        // تبدیل اعداد فارسی و عربی به لاتین
        let query = convertDigitsToLatin(event.target.value.trim());
        state.lastQuery = query;

        // پاک کردن تایمر قبلی
        clearTimeout(state.searchTimeout);

        // حداقل طول جستجو
        if (query.length < config.minSearchLength) {
            hideSearchResults();
            return;
        }

        // نمایش وضعیت در حال جستجو
        showSearchLoading();

        // تنظیم تایمر جدید با تاخیر
        state.searchTimeout = setTimeout(() => {
            // اگر کوئری تغییر نکرده باشد
            if (query === state.lastQuery) {
                searchMembers(query);
            }
        }, config.debounceTime);
    }

    async function searchMembers(query) {
        if (state.isSearching) return;
        state.isSearching = true;

        try {
            const url = new URL(config.searchMembersUrl);
            url.searchParams.append('q', query);

            const response = await fetch(url.toString(), {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            if (!response.ok) {
                throw new Error(`خطای شبکه: ${response.status} ${response.statusText}`);
            }

            const data = await response.json();
            renderSearchResults(data.members || []);
        } catch (error) {
            console.error('Search error:', error);
            showSearchError('خطا در دریافت نتایج: ' + error.message);
        } finally {
            state.isSearching = false;
        }
    }

    function renderSearchResults(members) {
        if (!members.length) {
            elements.searchResults.innerHTML = '<div class="search-result-item">هیچ عضوی یافت نشد</div>';
            elements.searchResults.style.display = 'block';
            return;
        }

        const html = members.map(member => `
            <div class="search-result-item" data-member-id="${member.id}">
                <div class="member-info">
                    <strong>${member.firstname} ${member.lastname}</strong>
                    <div>کد ملی: ${member.melicode}</div>
                </div>
                <div class="member-phone">تلفن: ${member.phonnumber}</div>
            </div>
        `).join('');

        elements.searchResults.innerHTML = html;
        elements.searchResults.style.display = 'block';
    }

    function handleSearchResultClick(event) {
        const resultItem = event.target.closest('.search-result-item');
        if (!resultItem) return;

        const memberId = resultItem.dataset.memberId;
        if (memberId) {
            // ارسال مستقیم به صفحه پروفایل با شناسه عضو
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/reserv/member_profile/';

            const memberIdInput = document.createElement('input');
            memberIdInput.type = 'hidden';
            memberIdInput.name = 'member_id';
            memberIdInput.value = memberId;
            form.appendChild(memberIdInput);

            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrfmiddlewaretoken';
            csrfInput.value = elements.csrfToken;
            form.appendChild(csrfInput);

            document.body.appendChild(form);
            form.submit();
        }
    }

    function handleOutsideClick(event) {
        const isClickInsideSearch = elements.memberSearch.contains(event.target);
        const isClickInsideResults = elements.searchResults.contains(event.target);

        if (!isClickInsideSearch && !isClickInsideResults) {
            hideSearchResults();
        }
    }

    // ==================== توابع کمکی ====================
    function hideSearchResults() {
        elements.searchResults.style.display = 'none';
    }

    function showSearchLoading() {
        elements.searchResults.innerHTML = '<div class="search-result-item loading">در حال جستجو...</div>';
        elements.searchResults.style.display = 'block';
    }

    function showSearchError(message) {
        elements.searchResults.innerHTML = `
            <div class="search-result-item error">
                ${message}
            </div>
        `;
        elements.searchResults.style.display = 'block';
    }
});