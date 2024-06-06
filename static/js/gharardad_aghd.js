var m =document.getElementById("melicodestekhdam");
var e = document.getElementById("etebarmelicod");
var f = document.getElementById("namemeli");
var gharar =document.getElementById("gharar");
var mozd = document.getElementById("mozd");
var typeselect = document.getElementById("typeselect");
var raveshpardakht = document.getElementById("raveshpardakht");
var job = document.getElementById("job");
var etebar = document.getElementById("etebar");
var melicodvalue = document.getElementById("melicodvalue")

    function melicodcheck(){
            f.hidden = true;
            gharar.hidden = true;
            mozd.hidden = true;
            job.hidden = true;
        if ( m.value  > 999999999 )
        {
            document.getElementById("face").click();
        }
    }
    if ( e.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});
    }
        if (e.innerHTML == "true") {
            f.hidden = false;
            gharar.hidden = false;
            mozd.hidden = true;
            job.hidden = true;
            m.value = melicodvalue.innerHTML
        }
    function checkmozd() {
        if (typeselect.value == "ساعتی") {
            mozd.hidden = false;
            raveshpardakht.innerHTML = "لطفا مبلغ دستمزد برای هر ساعت را به ریال  وارد کتید";

        }
        if (typeselect.value == "درصدی") {
            mozd.hidden = false;
            job.hidden = false;
            raveshpardakht.innerHTML = "درصد مورد نظر برای فعالیت انتخاب شده";

        }
        if (typeselect.value == "موردی") {
            mozd.hidden = false;
            job.hidden = false;
            raveshpardakht.innerHTML = "دستمزد مورد نظر برای فعالیت انتخاب شده";

        }
        if (typeselect.value == "ماهانه") {
            mozd.hidden = false;
            raveshpardakht.innerHTML = "لطفا مبلغ دستمزد برای هر ماه را به ریال  وارد کتید";

        }
    }
    if ( etebar.innerHTML == 'true' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'فعالیت مورد نظر با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }
    function redirectt() { window.location = "/"; }

