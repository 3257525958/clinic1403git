var etebarit = document.getElementById('etebarit');
var        f = document.getElementById("face");

        if (etebarit.innerHTML == "true") {
            Swal.fire({
                position: 'top-end',
                icon: 'success',
                title: 'با موفقیت ثبت شد',
                showConfirmButton: false,
                timer: 2000
            });
            console.log("2")
            setTimeout('redirectt()', 1000);
        }
    // }

        function redirectt() { window.location = "/"; }


        function chengh(){
        f.click()

}