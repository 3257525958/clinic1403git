mablagh = document.getElementById("mablaghpardakht");

function pardakhtcheng(){
        b = ((mablagh.value - (mablagh.value % 10 )) / 10);
    document.getElementById("pardakhtimablagh").innerHTML = (b).num2persian() + " " + "تومان";
    }

horofbaghimande = document.getElementById("horofbaghimande").innerHTML;
h = ((horofbaghimande - (horofbaghimande % 10 )) / 10);
document.getElementById("pardakhtimablagh").innerHTML = (h).num2persian() + " " + "تومان";

horofbestankari = document.getElementById("horofbestankari").innerHTML;
hh = ((horofbestankari - (horofbestankari % 10 )) / 10);
document.getElementById("bestankari").innerHTML = (hh).num2persian() + " " + "تومان";

horofbedehkari = document.getElementById("horofbedehkari").innerHTML;
hhh = ((horofbedehkari - (horofbedehkari % 10 )) / 10);
document.getElementById("bedehkari").innerHTML = (hhh).num2persian() + " " + "تومان";

horofjamkol = document.getElementById("horofjamkol").innerHTML;
hhhh = ((horofjamkol - (horofjamkol % 10 )) / 10);
document.getElementById("jamfactorhorof").innerHTML = (hhhh).num2persian() + " " + "تومان";
