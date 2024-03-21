var error = document.getElementById("error");

    if ( error.innerHTML == 'inject_botax') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفااطلاعات مربوط به سابقه ی تزریق بوتاکس را وارد کنید'
        })
    }
    if ( error.innerHTML == 'illnes') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفااطلاعات مربوط به سابقه ی بیماریاتان را وارد کنید'
        })
    }
    if ( error.innerHTML == 'sensivety') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفااطلاعات مربوط به سابقه ی حساسیت را وارد کنید'
        })
    }
    if ( error.innerHTML == 'pregnancy') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفااطلاعات مربوط به باردار بودنتان را وارد کنید'
        })
    }
    if ( error.innerHTML == 'imgshow') {
        Swal.fire({
            icon: 'warning',
            title: 'درباره استفاده از تصویرتان لطفا گزینه مورد نظرتان راانتخاب کنید'
        })
    }
    if ( error.innerHTML == 'satisfact') {
        Swal.fire({
            icon: 'warning',
            title: 'فایل مربوط به عوارض احتمالی را مطالعه نموده و تیک مورد نظر را بزنید'
        })
    }
