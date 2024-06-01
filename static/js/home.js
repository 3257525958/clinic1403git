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
