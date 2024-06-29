var job = document.getElementById("job");
var melicode = document.getElementById("melicode");
var jobbuttom =document.getElementById("jobbuttom");
var melicodesave= document.getElementById("melicodesave");
var jobsave = document.getElementById("jobsave");
var lpersonreserv = document.getElementById("lpersonreserv");
var lcastreserv = document.getElementById("lcastreserv");
var personreserv = document.getElementById("personreserv");
var castreserv = document.getElementById("castreserv");
var etebarmelicod = document.getElementById("etebarmelicod");
function chengejob(){
    jobbuttom.click();
}
    function melicodcheck(){
            document.getElementById("workhide").hidden = true;
            document.getElementById("detalhiden").hidden = true ;
        if ( document.getElementById("melicode").value.length  > 9 ) {
            jobbuttom.click();
        }
 }
    if ( etebarmelicod.innerHTML == 'false'){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});

    }
     if (etebarmelicod.innerHTML == 'true'){
            document.getElementById("workhide").hidden = false ;
            document.getElementById("detalhiden").hidden = false ;
            melicode.value = melicodesave.innerHTML;
            job.value = jobsave.innerHTML;
     }
         function redirectt()
    {
        window.location = "/";
    }
    console.log("hhhhhhhhhh");
    if (document.getElementById("etebarreservdasti").innerHTML == 'true'){
        console.log("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk");
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'رزرو با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',900);

    }



