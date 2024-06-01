var etebarit = document.getElementById('etebarit');
    console.log(etebarit.innerHTML)
    // function itetebar() {
    //     console.log("1")
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
        f = document.getElementById("face");
        f.click()

}