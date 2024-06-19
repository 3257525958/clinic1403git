
var etebarmelicod = document.getElementById("etebarmelicod");
var melicodvarizande = document.getElementById("melicodevarizande");
var job = document.getElementById("job");
var codemeli = document.getElementById("codemeli");
var  py = document.getElementById("py");
var  by = document.getElementById("by");
var  off = document.getElementById("off");
var hesab = document.getElementById("hesab");
var operator = document.getElementById("operator");
var offer = document.getElementById("offer");
var ca = document.getElementById("ca");
var cast = document.getElementById("cast");
var beyane = document.getElementById("beyane");
var  pardakht = document.getElementById("pardakht");
var klak = document.getElementById("klak");

            v = ((ca.value - (ca.value % 10 )) / 10);
            pardakht.value = cast.value - beyane.value - v*10 ;
            // klak.innerHTML = (1000).num2persian() + " " + "تومان";

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
function chengh(){
        melicodvarizande.value = codemeli.innerHTML;
        f = document.getElementById("face");
        f.click()

}
        function mablaghcheng(){
            b = ((ca.value - (ca.value % 10 )) / 10);
            lmablagh.innerHTML = (b).num2persian() + " " + "تومان";
            pardakht.value = cast.value - beyane.value - b*10 ;
            klak.innerHTML = (pardakht.value).num2persian() + " " + "تومان";

    }
