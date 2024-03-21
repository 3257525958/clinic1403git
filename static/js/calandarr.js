 function yearselect(v) {
    console.log(v);
    a = v /1000;
    console.log(a);
    if (a >= 1 ){
        f = document.getElementById("face");
        f.click();
       move();
     }
 }
 function move() {
    var elem = document.getElementById("myBar");
    var width = 0;
    var id = setInterval(frame, 20);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        elem.hidden=true
      } else {
        width++;
        elem.style.width = width + '%';
        elem.innerHTML = width * 1  + '%';
        elem.hidden=false
      }
    }
  }

