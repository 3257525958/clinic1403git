var m1 = document.getElementById("m1");
var m2 = document.getElementById("m2");
var m3 = document.getElementById("m3");
var m4 = document.getElementById("m4");
var m11 = document.getElementById("m11");
var m22 = document.getElementById("m22");
var m33 = document.getElementById("m33");
var m44 = document.getElementById("m44");
var l = document.getElementById("loglevel").innerHTML;
var x = document.getElementById("m44").innerHTML;
console.log(x);
console.log(l);
console.log("llllllllllllllllllll");
    if ( l == "مدیر");
       {
        m1.hidden = true;
        m2.hidden = true;
        m3.hidden = true;
        m4.hidden = true;
        m11.hidden = true;
        m22.hidden = true;
        m33.hidden = true;
        m44.hidden = true;
    }
        if ( l == "تولید محتوا") {
        m1.hidden = true;
        m2.hidden = false;
        m3.hidden = false;
        m4.hidden = true;
        m11.hidden = true;
        m22.hidden = false;
        m33.hidden = false;
        m44.hidden = true;
    }
        if ( l == "دسترسی معمولی") {
        m1.hidden = true;
        m2.hidden = true;
        m3.hidden = true;
        m4.hidden = true;
        m11.hidden = true;
        m22.hidden = true;
        m33.hidden = true;
        m44.hidden = true;
    }
        console.log(m44.innerHTML);
        console.log(m44.hidden);
        console.log(m4.innerHTML);
        console.log(m4.hidden);