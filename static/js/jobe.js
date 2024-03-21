
var newjobetebar = document.getElementById("newjobetebar");
var newemployetebar = document.getElementById("newemployetebar");
var deletjobetebar = document.getElementById("deletjob");
var lenjob = document.getElementById('lenjob');
var useretebar = document.getElementById('useretebar');
var employeeetebar = document.getElementById('employeeetebar');
var employeemessage = document.getElementById('employeemessage');
var deletemployetebar = document.getElementById('deletemployetebar');
var selectjob = document.getElementById('selectjob');
var deletworkmessage = document.getElementById('deletworkmessage');
var addetebar = document.getElementById('addetebar');
var    j = ( lenjob.innerHTML  * 19 ) + 100 ;
    console.log(addetebar);

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

    if ( newjobetebar.innerHTML == 'false') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا فعالیت مورد نظرتان را وارد کنید'
        })
    }
    if ( newemployetebar.innerHTML == 'false') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا عنوان کارمند را وارد کنید'
        })
    }

    if ( newjobetebar.innerHTML == 'repeat') {
        Swal.fire({
            icon: 'warning',
            title: 'فعالیت وارد شده تکراری است لطفا فعالیت جدید وارد کنید'
        })
    }

    function redirectt() { window.location = "/"; }

    if ( deletjobetebar.innerHTML == 'delet' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'فعالیت مورد نظر با موفقیت حذف گردید',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }


        if ( deletjobetebar.innerHTML == 'ok') {
        Swal.fire({
            icon: 'warning',
            title: 'یک فعالیت برای حذف انتخاب کنید'
        })
    }
        if ( useretebar.innerHTML == 'empty') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا کد ملی کارمند مورد نظر را وارد کنید'
        })
    }

    if ( useretebar.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});
    }
        if ( employeeetebar.innerHTML == 'ok') {
        Swal.fire({
            icon: 'warning',
            title: 'یک فعالیت انتخاب کنید'
        })
    }
    var m = employeemessage.innerHTML;
    if ( employeeetebar.innerHTML == 'addmployee' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: m + 'با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }
    if ( employeeetebar.innerHTML == 'repeat' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: m + 'قبلا ثبت شده است ',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }

        if ( deletemployetebar.innerHTML == 'empty') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا کد ملی کارمند مورد نظر را وارد کنید'
        })
    }
        if ( deletemployetebar.innerHTML == 'emptyjob') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا یکی از مشاغل کارمند مورد نظر رابرای حذف انتخاب کنید'
        })
    }
        if ( deletemployetebar.innerHTML == 'false') {
        Swal.fire({
            icon: 'warning',
            title: 'کد ملی وارد شده جز کارمندان تعریف نشده است'
        })
        // setTimeout('redirectt()',1000);
    }

    if ( deletemployetebar.innerHTML == 'delet' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'حدف شغل از کارمند مورد نظر با موفقیت انجام شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }
        if ( deletemployetebar.innerHTML == 'true') {
            deletemployee()
    }
    if ( deletworkmessage.innerHTML == 'false' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'حدف خدمت مورد نظر با موفقیت انجام شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }

        if ( selectjob.innerHTML == 'true') {
            servic()
    }
    if ( addetebar.innerHTML == 'cast') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا قیمت خدمت را وارد کنید'
        })
    }
    if ( addetebar.innerHTML == 'detalejob') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا جزئیات خدمت را وارد کنید'
        })
    }
    if (addetebar.innerHTML == 'succes' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'خدمت مورد نظر با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }

function addjob() {
    document.getElementById('textobject').innerHTML = "تعریف فعالیت جدید";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = "260px";

    document.getElementsByClassName('newjob')[0].hidden = false;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('newjob')[4].hidden = true;
    document.getElementsByClassName('newjob')[5].hidden = true;
    document.getElementsByClassName('newjob')[6].hidden = true;

    document.getElementsByClassName('regesterbuttonsave')[0].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[0].style.top = "190px";
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[4].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[6].hidden = true;
    document.getElementById('te').hidden = true;

    document.getElementById('regesterbuttoncancel').style.top = "190px";
}
function deletjob() {
    document.getElementById('textobject').innerHTML = "حذف فعالیت از لیست";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = j+70+"px";

    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = false;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('newjob')[4].hidden = true;
    document.getElementsByClassName('newjob')[5].hidden = true;
    document.getElementsByClassName('newjob')[6].hidden = true;

    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[1].style.top = j+"px";
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[4].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[6].hidden = true;

    document.getElementById('regesterbuttoncancel').style.top = j+"px";
    document.getElementById('te').hidden = true;
}
function addemployee() {
    document.getElementById('textobject').innerHTML = "تعریف نیروی جدید برای فعالیتها";
    document.getElementById('regester').style.height = j+130+"px";
    document.getElementById('regester').hidden = false;

    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = false;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('newjob')[4].hidden = true;
    document.getElementsByClassName('newjob')[5].hidden = true;
    document.getElementsByClassName('newjob')[6].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[2].style.top = j+50+"px";
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[4].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[6].hidden = true;

    document.getElementsByClassName('inputclass')[2].style.top = j+"px";
    document.getElementById('regesterbuttoncancel').style.top = j+50+"px";
    document.getElementById('te').hidden = true;
}
function melicodesearch() {
    document.getElementById('textobject').innerHTML = "حذف نیرو از لیست";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = "200px";

    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = false;
    document.getElementsByClassName('newjob')[4].hidden = true;
    document.getElementsByClassName('newjob')[5].hidden = true;
    document.getElementsByClassName('newjob')[6].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[4].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[4].style.top = "130px";
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[6].hidden = true;

    document.getElementById('regesterbuttoncancel').hidden = true;
}
function deletemployee() {
    document.getElementById('textobject').innerHTML = "حذف نیرو از لیست ";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = j+130+"px";

    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('newjob')[4].hidden = false;
    document.getElementsByClassName('newjob')[5].hidden = true;
    document.getElementsByClassName('newjob')[6].hidden = true;

    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[3].style.top = j+50+"px";
    document.getElementsByClassName('regesterbuttonsave')[4].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[6].hidden = true;

    document.getElementById('regesterbuttoncancel').style.top = j+50+"px";
    document.getElementById('te').hidden = false;
}
function servic() {
    document.getElementById('textobject').innerHTML = "تعریف یک خدمت  ";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = "500px";

    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('newjob')[4].hidden = true;
    document.getElementsByClassName('newjob')[5].hidden = false;
    document.getElementsByClassName('newjob')[6].hidden = true;

    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[4].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[5].style.top = "430px";
    document.getElementsByClassName('regesterbuttonsave')[6].hidden = true;

    document.getElementById('regesterbuttoncancel').hidden = false;
    document.getElementById('regesterbuttoncancel').style.top = "430px";
    document.getElementById('te').hidden = true;
    document.getElementById("textemployname").hidden =false;
    document.getElementById("sel").hidden = false;
    document.getElementById("time").hidden = false;
}
function deletservic(){
    document.getElementById('textobject').innerHTML = "حذف یک خدمت  ";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = "200px";

    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('newjob')[4].hidden = true;
    document.getElementsByClassName('newjob')[5].hidden = true;
    document.getElementsByClassName('newjob')[6].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[4].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[5].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[6].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[6].style.top = "130px";

    document.getElementById('regesterbuttoncancel').hidden = false;
    document.getElementById('regesterbuttoncancel').style.top = "130px";

}
function citylist()
{
        f = document.getElementById("face");
        f.click()
}

