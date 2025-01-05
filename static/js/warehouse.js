var lmablagh = document.getElementById("lmablagh");
var mablagh = document.getElementById("mablagh");
var takhfif = document.getElementById("takhfif");

function mablaghcheng(){
        b = ((mablagh.value - (mablagh.value % 10 )) / 10);
    lmablagh.innerHTML = (b).num2persian() + " " + "تومان";
    }
function chenghselect(){
    document.getElementById("btf").click()
}


function mablaghtakhfif(){
        c = ((takhfif.value - (takhfif.value % 10 )) / 10);
    document.getElementById("ltakhfif").innerHTML = (c).num2persian() + " " + "تومان";
    }
