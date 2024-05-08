var m1 = document.getElementById("m1");
var m2 = document.getElementById("m2");
var m3 = document.getElementById("m3");
var m4 = document.getElementById("m4");
var l = document.getElementById("loglevel").innerHTML;
console.log(l);
console.log(",mmmmm");
    if ( l == "مدیر");
       {
        m1.hidden = true;
        m2.hidden = true;
        m3.hidden = true;
        m4.hidden = true;
    }
        if ( l == "تولید محتوا") {
        m1.hidden = true;
        m2.hidden = false;
        m3.hidden = false;
        m4.hidden = true;
    }
        if ( l == "دسترسی معمولی") {
        m1.hidden = false;
        m2.hidden = false;
        m3.hidden = false;
        m4.hidden = false;
    }