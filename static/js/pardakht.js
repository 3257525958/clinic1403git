function cilik(){
    document.getElementById("btfpardakht").click();
}

if ( document.getElementById("timechek").innerHTML == 'true'){
    document.getElementById("bazezamani").hidden = false;
}

if ( document.getElementById("materialchek").innerHTML == 'true'){
    document.getElementById("materiallist").hidden = false;
}
if ( document.getElementById("foroshchek").innerHTML == 'true'){
    document.getElementById("foroshandelist").hidden = false;
}
if ( document.getElementById("factorchek").innerHTML == 'true'){
    document.getElementById("factornumber").hidden = false;
}