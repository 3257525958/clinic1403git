var savebtn = document.getElementById("savebtn");


    if ( savebtn.innerHTML == 'true' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'عضو جدید با موفقیت تغییر کرد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',500);
    }

    if ( savebtn.innerHTML == 'repeat' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'این عضو قبلا ثبت شده است',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',500);
    }

    function redirectt()
    {
        window.location = "/";
    }
