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
var offermeghdar = document.getElementById("offermeghdar");
var lmablaghbeyane = document.getElementById("lmablaghbeyane");
var beyanemeghdar = document.getElementById("beyanemeghdar");
var inputid = document.getElementById("inputid");
var lableid = document.getElementById("lableid");
var isearchname = document.getElementById("namesearch");
var la = document.getElementById('la');
var ia = document.getElementById('ia');
var etebarsabt = document.getElementById("etebarsabt");
    if ( etebarsabt.innerHTML == 'true' ){
        console.log("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii");
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'فعالیت مورد نظر با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }
    function redirectt() { window.location = "/"; }


    if ( etebarname.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});
    }
        melicodsearch.value = codemeli.innerHTML;
        ia.value = la.innerHTML;
        // isearchname.value = lsearchname.innerHTML;
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
    function mablagh(){
        b = ((offermeghdar.value - (offermeghdar.value % 10 )) / 10);
        inputid.value = lableid.innerHTML;
        lmablagh.innerHTML = (b).num2persian() + " " + "تومان";
    }
    function mablaghbeyane(){
        b = ((beyanemeghdar.value - (beyanemeghdar.value % 10 )) / 10);

    lmablaghbeyane.innerHTML = (b).num2persian() + " " + "تومان";
    }
    function clk(){
            document.getElementById("tik").click();
    }
    function load() {
        j = document.getElementById("jamekol").value
        bb = ((j - (j % 10)) / 10);
        document.getElementById("ljamkol").innerHTML = (bb).num2persian() + " " + "تومان";
    }
    function searchnamefun(){
        if ( isearchname.value.length > 2)
            document.getElementById("searchnamebottum").click();

}
    function btndayselectfun(){
        document.getElementById("btndayselect").click();
    }
    function btnmounthselectfun(){
        document.getElementById("btnmounthselect").click();
    }
