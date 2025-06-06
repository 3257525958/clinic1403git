
etebar_edit = document.getElementById("etebar_edit");
        console.log(etebar_edit.innerHTML);
if ( etebar_edit.innerHTML == 'succes' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'ویرایش با موفقیت انجام شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',500);
    }

if (etebar_edit.innerHTML == 'ok' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'ویرایش با موفقیت انجام شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('profile()',500);
    }
    function profile()
    {
        window.location = "/reserv/member_profile/";
    }
    function redirectt()
    {
        window.location = "/";
    }
