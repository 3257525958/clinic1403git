var job = document.getElementById("job");
var melicode = document.getElementById("melicode");
var jobbuttom =document.getElementById("jobbuttom");
var melicodesave= document.getElementById("melicodesave");
var jobsave = document.getElementById("jobsave");
var personreserv = document.getElementById("personreserv");
var castreserv = document.getElementById("castreserv");
var etebarmelicod = document.getElementById("etebarmelicod");
var namebuttom = document.getElementById("namebuttom");
var names = document.getElementById("names");
var etebarreservdasti = document.getElementById("etebarreservdasti");
var personelbutton = document.getElementById("personelbutton");
        function chengejob(){
    jobbuttom.click();
}
        function chengepersonel(){
            personelbutton.click()
        }
        function melicodcheck(){
            document.getElementById("sendbtn").hidden = true;
            document.getElementById("namepersonel").hidden = true;
            document.getElementById("workhide").hidden = true;
            document.getElementById("detalhiden").hidden = true ;
            document.getElementById("peyment").hidden = true ;
            document.getElementById("m1").hidden = true ;
            document.getElementById("bey").hidden = true ;
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
        console.log(etebarmelicod.innerHTML);
        if (etebarmelicod.innerHTML == 'true'){
            document.getElementById("sendbtn").hidden = false;
            document.getElementById("namepersonel").hidden = false;
            document.getElementById("workhide").hidden = false ;
            document.getElementById("detalhiden").hidden = false ;
            document.getElementById("peyment").hidden = false ;
            document.getElementById("m1").hidden = false ;
            document.getElementById("bey").hidden = false ;
            melicode.value = melicodesave.innerHTML;
            job.value = jobsave.innerHTML;
     }
        function redirectt() {
        window.location = "/";
    }
        // console.log(etebarreservdasti.innerHTML);
        if ( etebarreservdasti.innerHTML == 'true' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'رزرو با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',900);

    }
        function namecheck(){
        if ( names.value.length > 2 ) {
        document.getElementById("table").hidden = false;
            namebuttom.click();
        }
 }
        function move(){
           Swal.fire({
              position: 'top-end',
              icon: 'success',
              title: 'رزرو با موفقیت ثبت شد',
              showConfirmButton: false,
              timer: 2000
                     });
        setTimeout('redirectt()',900);
        }
        function clickteak(){
        document.getElementById("buttomteakclick").click();
    }
        function jobclick(){
            console.log(document.getElementById("job").innerHTML);
            document.getElementById("jobbuttom").click();
        }

    function mablaghbeyane(){
        b = ((beyanemeghdar.value - (beyanemeghdar.value % 10 )) / 10);
        inputid.value = lableid.innerHTML;
        lmablaghbeyane.innerHTML = (b).num2persian() + " " + "تومان";
    }

