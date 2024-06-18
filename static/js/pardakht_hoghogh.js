var table = document.getElementById("table");
var m = document.getElementById("melicodestekhdam");
var e= document.getElementById("etebarmelicod");
var melicodvalue = document.getElementById("melicodvalue");
var f = document.getElementById("namemeli");
var mounthselect = document.getElementById("mounthselect");
var munt = document.getElementById("munt");
var table = document.getElementById("table");
var jam = document.getElementById("jam");
var tick = document.getElementById("tick");
var notsel = document.getElementById("notsel");
var sel = document.getElementById("sel");
var tickon = document.getElementById("tickon");
var tickoff = document.getElementById("tickoff");
    // console.log(tick.value);
    // console.log(tick.innerHTML);
    function melicodcheck(){
            table.hidden = true;
            f.hidden = true;
        if ( m.value.length  > 9 )
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
            table.hidden = false;
            m.value = melicodvalue.innerHTML;
            munt.value = mounthselect.innerHTML;
        }
    function clicon(){
        notsel.value = tickon.value;
        document.getElementById("face").click();
    }
    function clicoff(){
        sel.value = tickoff.value;
        document.getElementById("face").click();
    }
    function redirectt() { window.location = "/"; }
