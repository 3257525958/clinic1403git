var reservetebar = document.getElementById("reservetebar");
var btn = document.getElementsByClassName("boxxx")[2];
var jadval =document.getElementById("jadval");
var operatoreselect = document.getElementById("operatoreselect");
var  etebar = document.getElementById("etebar");
var mounthchek = document.getElementById("mounthchek");
    //     if (mounthchek.innerHTML == 'false'){
    //     Swal.fire({
    //       position: 'top-end',
    //       icon: 'success',
    //       title: 'ماههای قبل قابل تغییر نیستند',
    //       showConfirmButton: false,
    //       timer: 4000
    //              });
    // setTimeout('redirectt()',2000);
    //     }
        if ( etebar.innerHTML == 'true'){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'مرخصی شما با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 4000
                 });


    setTimeout('redirectt()',2000);
    }
        if ( reservetebar.innerHTML == 'false2') {
        Swal.fire({
            icon: 'warning',
            title: 'خدمتی که انتخاب کرده اید یک ساعت به طول می انجامد باید در جدول زمانبندی زمانی را انتخاب کنید که تایم بعد از آن هم خالی باشد '
        })
    }
function clic(){
           document.getElementById("daysave").value = document.getElementById("today").innerHTML
}
        function operatoreclick(){
            document.getElementById("operatorebuttom").click();
        }

    function redirectt()
    {
        window.location = "/";
    }
