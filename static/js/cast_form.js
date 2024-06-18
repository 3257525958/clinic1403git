
var etebarmelicod = document.getElementById("etebarmelicod");
var melicodvarizande = document.getElementById("melicodevarizande");
var job = document.getElementById("job");
var codemeli = document.getElementById("codemeli");
var  py = document.getElementById("py");
var  by = document.getElementById("by");
var  off = document.getElementById("off");
var hesab = document.getElementById("hesab");
var operator = document.getElementById("operator");


    function melicodcheck(){
        py.hidden = true;
        job.hidden = true;
        by.hidden = true;
        off.hidden = true;
        hesab.hidden = true;
        operator.hidden = true;
        if ( melicodvarizande.value.length  > 9 )
        {
            document.getElementById("faceb1").click();
        }
    }

    if ( etebarmelicod.innerHTML == 'false') {
        Swal.fire({
            icon: 'warning',
            title: 'کد ملی وارد شده قبلا ثبت نام نکرده است'
        })
    }
    if ( etebarmelicod.innerHTML == 'true') {
        job.hidden = false;
        py.hidden = false;
        by.hidden = false;
        hesab.hidden = false;
        operator.hidden = false;
        off.hidden = false;
        melicodvarizande.value = codemeli.innerHTML;

    }

    // if ( newjobetebar.innerHTML == 'ok' ){
    //     Swal.fire({
    //       position: 'top-end',
    //       icon: 'success',
    //       title: 'فعالیت مورد نظر با موفقیت ثبت شد',
    //       showConfirmButton: false,
    //       timer: 2000
    //              });
    //     setTimeout('redirectt()',1000);
    // }


function chengh(){
        melicodvarizande.value = codemeli.innerHTML;
        f = document.getElementById("face");
        f.click()

}
