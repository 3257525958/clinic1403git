
var etebarmelicod = document.getElementById("etebarmelicod");

    console.log(etebarmelicod.innerHTML);

    if ( etebarmelicod.innerHTML == 'false') {
        Swal.fire({
            icon: 'warning',
            title: 'کد ملی وارد شده قبلا ثبت نام نکرده است'
        })
    }

    if ( newjobetebar.innerHTML == 'ok' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'فعالیت مورد نظر با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }

function citylist()
{
        x = document.getElementById("cast")
        x.value = "سلام داداش گلم"
        f = document.getElementById("face");
        f.click()
}

function chengh(){
        f = document.getElementById("face");
        f.click()

}