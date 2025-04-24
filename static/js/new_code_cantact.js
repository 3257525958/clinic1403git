    let minutes = 1;
    let seconds = 0;
    let set_inteval;
    const etebar = document.getElementById("etebar");

    function otp_timer() {
        seconds--;

        if(seconds < 0) {
            minutes--;
            seconds = 59;
        }

        document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
        document.getElementById('minutes').textContent = minutes;

        if(minutes === 0 && seconds === 0) {
            clearInterval(set_inteval);
            document.getElementById('regesterbuttonrepeat').disabled = false;
            document.getElementById('regesterbuttonrepeat').classList.remove('cancel-btn');
            document.getElementById('regesterbuttonrepeat').classList.add('pay-btn');
        }
    }

    function startTimer() {
        document.getElementById('regesterbuttonrepeat').disabled = true;
        document.getElementById('regesterbuttonrepeat').classList.remove('pay-btn');
        document.getElementById('regesterbuttonrepeat').classList.add('cancel-btn');
        minutes = 1;
        seconds = 0;
        set_inteval = setInterval(otp_timer, 1000);
    }

    // شروع تایمر اولیه
    startTimer();

    // مدیریت ارسال مجدد
    document.getElementById('regesterbuttonrepeat').addEventListener('click', () => {
        // کد ارسال مجدد
        startTimer();
    });

    // مدیریت اعتبارسنجی کد
    // function validateCode() {
    //     const code = document.getElementById('verificationCode').value;
    //     if(code.length === 4 && !isNaN(code)) {
    //         // ارسال به سرور
    //         // window.location.href = '/success-page';
    //     }
    // }
var etebar = document.getElementById("etebar");
if ( etebar.innerHTML == 'succes' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'با موفقیت وارد شدید',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',500);
    }
    function redirectt()
    {
        window.location = "/";
    }
