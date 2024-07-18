var reservetebar = document.getElementById("reservetebar");
var btn = document.getElementsByClassName("boxxx")[2];
var jadval =document.getElementById("jadval");
var operatoreselect = document.getElementById("operatoreselect");

        if ( reservetebar.innerHTML == 'false2') {
        Swal.fire({
            icon: 'warning',
            title: 'خدمتی که انتخاب کرده اید یک ساعت به طول می انجامد باید در جدول زمانبندی زمانی را انتخاب کنید که تایم بعد از آن هم خالی باشد '
        })
    }
function clic(){
           document.getElementById("daysave").value = document.getElementById("today").innerHTML
}
        function operatoreclick(){
            document.getElementById("operatorebuttom").click();
        }
