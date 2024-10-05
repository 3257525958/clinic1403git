//                 document.getElementById("textsend").click();
//                 document.getElementById("textsend").value = document.getElementById("texttextttt").innerHTML;
//                 document.getElementById("textsend").click();
// function  cklik(){
//                 document.getElementById("textsend").click();
//                 document.getElementById("check").click();
//                 document.getElementById("textsend").click();
// }
// function startTimer() {
//     document.getElementById("textsend").click();
//     set_inteval = setInterval( 'cklik()', 6000 );
// }
// startTimer();
// if (document.getElementById("texttextttt").innerHTML == ' ') {
//         document.getElementById("textsend").click();
//
// }
// document.getElementById("textsend").click();
//
//
//
DB_HOST : 'd1403-6-sjp-service'
DB_PORT : 'django.db.backends.mysql'
DB_DATABASE : 'd1403-6qbg_db'
DB_USERNAME : 'root'
DB_PASSWORD :'krOenXvXrTN8WwUpr57q'

// process.env.DB_HOST
var mysql = require ('mysql');

var con = mysql.createConnection({
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'd1403-6qbg_db',
    'USER': 'root',
    'PASSWORD': 'krOenXvXrTN8WwUpr57q',
    'HOST': 'd1403-6-sjp-service',
});
con.connect((err) => {
  if (err) throw err;
  console.log('Connected!');
});