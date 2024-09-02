

function time() {
var MyDate = new Date();
var MyDateshamsi = new Date().toLocaleDateString('fa-IR');
    document.getElementById("date").value = MyDateshamsi;
    document.getElementById("thours").value = MyDate.getHours();
    document.getElementById("tminutes").value = MyDate.getMinutes();
    document.getElementById("tseconds").value = MyDate.getSeconds();
    if (MyDate.getMinutes() == 25) {
        if ( MyDate.getSeconds() == 2) {
            document.getElementById("btndate").click();
        }
    }
}

setInterval(time, 1000);
document.addEventListener('DOMContentLoaded', function() {
    if ( screen > 601){
        var  a = 5000} else { var a = 0}

    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {
      edge : "right"
    });


    var carouselElems = document.querySelectorAll('.carousel');
    M.Carousel.init(carouselElems, {

      fullWidth : true ,
      indicators : true ,
      onCycleTo : function(){
        let el = document.querySelectorAll('.text_style');
        for (const item of el) {
          item.classList.remove('isShow');
          setTimeout(function(){
            item.classList.add('isShow');
          },700)
        }
      },
    });
    setInterval(function(){
      M.Carousel.getInstance(carouselElems[0]).next()
    }, 2000)
  })

