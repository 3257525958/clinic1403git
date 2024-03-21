const menuo = document.querySelector(".imgnavbarmenuo");
const visib = document.querySelector(".menuo");
var loginetebar = document.getElementById("loginetebar");

var c = false
function visiblemenuo(){
    if (c == false){
        visib.style.visibility="visible";
        console.log(c);
    }
    if (c == true){
        visib.style.visibility="hidden";
        console.log(c);
    }
    switch (c){
        case false: c = true;
             break;
        case true: c = false;
             break;        
    }

}

var slideIndex = 0;

showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
     }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
     }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 4000); // Change image every 2 seconds
}


function menuooo() {
    if (c == false){
        visib.style.visibility="visible";
        console.log(c);
    }
    if (c == true){
        visib.style.visibility="hidden";
        console.log(c);
    }
    switch (c){
        case false: c = true;
             break;
        case true: c = false;
             break;
    }

}
    if ( loginetebar.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'برای رزرو ابتدا باید به حساب کاربری وارد شوید',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});
                        setTimeout('redirectt()',1000);

    }

var etebar = document.getElementById("etebar");
    if ( etebar.innerHTML == 'succes' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'رمز با موفقیت تغییر کرد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',500);
    }


    function redirectt() { window.location = "/"; }
