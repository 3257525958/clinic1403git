var lmablagh = document.getElementById("lmablagh");
var mablagh = document.getElementById("mablagh");


function mablaghcheng(){
        b = ((mablagh.value - (mablagh.value % 10 )) / 10);
    lmablagh.innerHTML = (b).num2persian() + " " + "تومان";
    }
function chenghselect(){
    document.getElementById("btf").click()
}