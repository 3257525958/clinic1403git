var m1 = document.getElementById("m1");
var m2 = document.getElementById("m2");
var m3 = document.getElementById("m3");
var m4 = document.getElementById("m4");
var m5 = document.getElementById("m5");
var m6 = document.getElementById("m6");
var m7 = document.getElementById("m7");
var m8 = document.getElementById("m8");
var m9 = document.getElementById("m9");
var m10 = document.getElementById("m10");
var m11 = document.getElementById("m11");
var m12 = document.getElementById("m12");
var m13 = document.getElementById("m13");
var m14 = document.getElementById("m14");
var m15 = document.getElementById("m15");
var m16 = document.getElementById("m16");
var m17 = document.getElementById("m17");
var m18 = document.getElementById("m18");
var m111 = document.getElementById("m111");
var m22 = document.getElementById("m22");
var m33 = document.getElementById("m33");
var m44 = document.getElementById("m44");
var m55 = document.getElementById("m55");
var m66 = document.getElementById("m66");
var m77 = document.getElementById("m77");
var m88 = document.getElementById("m88");
var m99 = document.getElementById("m99");
var m1010 = document.getElementById("m1010");
var m1111 = document.getElementById("m1111");
var m1212 = document.getElementById("m1212");
var m1313 = document.getElementById("m1313");
var m1414 = document.getElementById("m1414");
var m1515 = document.getElementById("m1515");
var m1616 = document.getElementById("m1616");
var m1717 = document.getElementById("m1717");
var m1818 = document.getElementById("m1818");


var l = document.getElementById("loglevel").innerHTML;
    if ( l == "مدیر");
       {
        m1.hidden = false;
        m2.hidden = false;
        // m3.hidden = false;
        // m4.hidden = false;
        // m5.hidden = false;
        // m6.hidden = false;
        m7.hidden = false;
        m8.hidden = false;
        m9.hidden = false;
        m10.hidden = false;
        m11.hidden = false;
        m12.hidden = false;
        m13.hidden = false;
        m14.hidden = false;
        m15.hidden = false;
        m16.hidden = false;
        m17.hidden = false;
        m18.hidden = false;
        m111.hidden = false;
        m22.hidden = false;
        m33.hidden = false;
        m44.hidden = false;
        m55.hidden = false;
        m66.hidden = false;
        m77.hidden = false;
        m88.hidden = false;
        m99.hidden = false;
        m1010.hidden = false;
        m1111.hidden = false;
        m1212.hidden = false;
        m1313.hidden = false;
        m1414.hidden = false;
        m1515.hidden = false;
        m1616.hidden = false;
        m1717.hidden = false;
        m1818.hidden = false;
    }
        if ( l == "تولید محتوا") {
        m1.hidden = false;
        m2.hidden = true;
        // m3.hidden = true;
        // m4.hidden = true;
        // m5.hidden = true;
        // m6.hidden = true;
        m7.hidden = true;
        m8.hidden = true;
        m9.hidden = true;
        m10.hidden = true;
        m12.hidden = false;
        m13.hidden = true;
        m111.hidden = false;

        m11.hidden = false;
        m22.hidden = true;
        m33.hidden = true;
        m44.hidden = true;
        m55.hidden = true;
        m66.hidden = true;
        m77.hidden = true;
        m88.hidden = true;
        m99.hidden = true;
        m1010.hidden = true;
        m1111.hidden = false;
        m1212.hidden = false;
        m1313.hidden = true;
    }
        if ( l == "دسترسی معمولی") {
        m1.hidden = false;
        m2.hidden = false;
        m3.hidden = true;
        m4.hidden = true;
        m5.hidden = true;
        m6.hidden = true;
        m7.hidden = true;
        m8.hidden = true;
        m9.hidden = true;
        m10.hidden = true;
        m111.hidden = true;
        m12.hidden = true;
        m13.hidden = true;

        m11.hidden = true;
        m22.hidden = true;
        m33.hidden = true;
        m44.hidden = true;
        m55.hidden = true;
        m66.hidden = true;
        m77.hidden = true;
        m88.hidden = true;
        m99.hidden = true;
        m1010.hidden = true;
        m1111.hidden = true;
        m1212.hidden = true;
        m1313.hidden = true;
    }
        if ( l == "رزروشن") {
        m1.hidden = false;
        m2.hidden = false;
        m3.hidden = true;
        m4.hidden = true;
        m5.hidden = true;
        m6.hidden = true;
        m7.hidden = false;
        m8.hidden = true;
        m9.hidden = true;
        m10.hidden = false;
        m111.hidden = true;
        m12.hidden = true;
        m13.hidden = true;

        m11.hidden = false;
        m22.hidden = false;
        m33.hidden = true;
        m44.hidden = true;
        m55.hidden = true;
        m66.hidden = true;
        m77.hidden = false;
        m88.hidden = true;
        m99.hidden = true;
        m1010.hidden = false;
        m1111.hidden = true;
        m1212.hidden = true;
        m1313.hidden = true;
    }
        if (l != "دسترسی معمولی" ) {
            if (l != "تولید محتوا") {
                if (l != "مدیر") {
                    if (l != "رزروشن") {
                        m1.hidden = false;
                        m2.hidden = true;
                        m3.hidden = true;
                        m4.hidden = true;
                        m5.hidden = true;
                        m6.hidden = true;
                        m7.hidden = true;
                        m8.hidden = true;
                        m9.hidden = true;
                        m10.hidden = true;
                        m111.hidden = true;
                        m12.hidden = true;
                        m13.hidden = true;
                        m14.hidden = true;
                        m15.hidden = true;
                        m16.hidden = true;
                        m17.hidden = true;
                        m18.hidden = true;


                        m11.hidden = false;
                        m22.hidden = true;
                        m33.hidden = true;
                        m44.hidden = true;
                        m55.hidden = true;
                        m66.hidden = true;
                        m77.hidden = true;
                        m88.hidden = true;
                        m99.hidden = true;
                        m1010.hidden = true;
                        m1111.hidden = true;
                        m1212.hidden = true;
                        m1313.hidden = true;
                        m1414.hidden = true;
                        m1515.hidden = true;
                        m1616.hidden = true;
                        m1717.hidden = true;
                        m1818.hidden = true;
                    }
                }
            }
        }

// var e=document.getElementById("tes");
var i=document.getElementById("ee");
var f =document.getElementById("tab");
    if ( i.value != window.outerWidth) {
        console.log("aaaaaaaaa");
        i.value = window.outerWidth;
        if (f.innerHTML == 0){
        e = document.getElementById("testes");
        e.click();
        console.log("qqqqqqqqq");}
    }