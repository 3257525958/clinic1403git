    var login_etebar = document.getElementById("login_etebar");
    console.log(login_etebar.innerHTML);


//     if ( login_etebar.innerHTML == 'true' ){
//         Swal.fire({
//           position: 'top-end',
//           icon: 'success',
//           title: 'با موفقیت وارد شدید',
//           showConfirmButton: false,
//           timer: 2500
//                  });
//         window.location = "/";
//         // window.open('http://drmahdiasadpour.ir','_self');
// }


    if ( login_etebar.innerHTML == 'false_in_paswoord' ){
        Swal.fire({
            icon: 'هشدار',
            title: 'رمز اشتباه است',
            text: 'برای ورود یا بازیابی رمز از لینک زیر استفاده کنید',
            footer: '<a href="/cantact/ignor/">فراموشی رمز</a>'
});
    }


    if ( login_etebar.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});
    }


    if ( login_etebar.innerHTML == 'empty' ){

        Swal.fire('لطفا کد ملی را وارد کنید');

    }


    if ( login_etebar.innerHTML == 'true' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'با موفقیت وارد شدید',
          showConfirmButton: false,
          timer: 4000
                 });


    setTimeout('redirectt()',2500);
    }


    function redirectt()
    {
        window.location = "/";
    }


