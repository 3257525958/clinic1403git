var m =document.getElementById("melicodestekhdam");
var e = document.getElementById("etebarmelicod");
var f = document.getElementById("namemeli");
var job = document.getElementById("job");
var etebar = document.getElementById("etebar");
var melicodvalue = document.getElementById("melicodvalue")
    function melicodcheck(){
            f.hidden = true;
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
            job.hidden = false;
            m.value = melicodvalue.innerHTML
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

