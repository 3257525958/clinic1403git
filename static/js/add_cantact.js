
    var etebar = document.getElementById("melicod_etebar");
    console.log(etebar.innerHTML);
    if ( etebar.innerHTML == 'false' ){ mymessage()}

    function mymessage(){
        Swal.fire({
              icon: 'هشدار',
              title: 'کد ملی وارد شده قبلا ثبت شده است',
              text: 'برای ورود یا بازیابی رمز از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/login/">ورود و بازیابی رمز</a>'
})
    }

    if ( etebar.innerHTML == 'empty')
    {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا کد ملی را وارد کنید'
        })

    }
    if ( etebar.innerHTML == 'repeat')
    {
        Swal.fire({
            icon: 'warning',
            title: 'کد ملی معتبر نمیباشد'
        })
    }
    if ( etebar.innerHTML == 'stringerror')
    {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا اعداد را انگلیسی وارد کنید'
        })

    }
    if ( etebar.innerHTML == 'tellerror')
    {
        Swal.fire({
            icon: 'warning',
            title: 'شماره تلفن اشتباه وارد شده است'
        })

    }


    if ( etebar.innerHTML == 'neterror')
    {
        Swal.fire({
            icon: 'warning',
            title: 'شبکه اینترنت شما متصل نمیشود'
        })

    }
