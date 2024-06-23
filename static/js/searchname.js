var inputsearchname = document.getElementById("inputsearchname");
var inputsearchmelicod = document.getElementById("inputsearchmelicod");
var melicodsearch = document.getElementById("melicodsearch");
var namesearch = document.getElementById("namesearch");
var facebuttonsearchname = document.getElementById("facebuttonsearchname");
var facesearchmelicode = document.getElementById("facesearchmelicode");
var lablesearchname = document.getElementById("lablesearchname");
var etebarname = document.getElementById("etebarname");
var table = document.getElementById("table");
var codemeli = document.getElementById("codemeli");


    console.log(melicodsearch.value);
    console.log("sssssssssssssssssssssss");
    if ( etebarname.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});
    }

        console.log(codemeli.innerHTML);
        melicodsearch.value = codemeli.innerHTML;
    if ( etebarname == "true" ){
        table.hidden = false;
    }

 function searchmelicodfun(){
        table.hidden = true;
     if ( melicodsearch.value.length > 9) {
         facesearchmelicode.click();
     }
 }
    function clickteak(){
        document.getElementById("buttomteakclick").click();
    }
