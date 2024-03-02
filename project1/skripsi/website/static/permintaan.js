document.addEventListener("DOMContentLoaded", function() {
    var save_permintaan_route = document.getElementById("save_permintaan_route").dataset.url;
    console.log(save_permintaan_route);
    // Ambil referensi ke elemen-elemen formulir
    var Form1 = document.getElementById("Form1");
    var Form2 = document.getElementById("Form2");
    var Form3 = document.getElementById("Form3");
    var Form4 = document.getElementById("Form4");
    var progress = document.getElementById("progress");
    var formdata = new FormData();

    // Fungsi untuk mengirim data formulir ke server
    function sendData(formData) {
        fetch(save_permintaan_route, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle response data, redirect or show success message
            redirectToSuccessPage();
        })
        .catch(error => {
            console.error(error);
        });
    }

    // Fungsi untuk memindahkan ke halaman berhasil
    function redirectToSuccessPage() {
        window.location.href = "/permintaan_berhasil";
    }

    // Fungsi untuk validasi formulir
    function validateForm(form) {
        var inputs = form.querySelectorAll('input');
        for (var i = 0; i < inputs.length; i++) {
            if (inputs[i].value.trim() === '') {
                console.log('Nilai input kosong pada index:', i); // Menampilkan indeks input yang kosong                
                alert('Silakan isi semua bidang yang diperlukan!');
                return false;
            }
        }
        return true;
    }

    // Fungsi untuk memindahkan ke formulir berikutnya
    function moveToNextForm(currentForm, nextForm, width) {
        if (validateForm(currentForm)) {
            currentForm.style.left = "-450px";
            nextForm.style.left = "40px";
            progress.style.width = width;
        }
    }

    // Fungsi untuk memindahkan ke formulir sebelumnya
    function moveToPreviousForm(currentForm, previousForm, width) {
        currentForm.style.left = "450px";
        previousForm.style.left = "40px";
        progress.style.width = width;
    }

    // Daftar penanganan acara klik untuk tombol navigasi formulir
    document.getElementById("Next1").addEventListener("click", function() {
        moveToNextForm(Form1, Form2, "180px");
    });

    document.getElementById("Next2").addEventListener("click", function() {
        moveToNextForm(Form2, Form3, "270px");
    });

    document.getElementById("Next3").addEventListener("click", function() {
        moveToNextForm(Form3, Form4, "360px");
    });

    document.getElementById("previous1").addEventListener("click", function() {
        moveToPreviousForm(Form2, Form1, "90px");
    });

    document.getElementById("previous2").addEventListener("click", function() {
        moveToPreviousForm(Form3, Form2, "180px");
    });

    document.getElementById("previous3").addEventListener("click", function() {
        moveToPreviousForm(Form4, Form3, "270px");
    });

    // Fungsi untuk menggabungkan data formulir ke FormData
    function mergeForm(form) {
        var inputs = form.querySelectorAll('input');
        for (var i = 0; i < inputs.length; i++) {
            formdata.append(inputs[i].name, inputs[i].value);
        }
    }

    // Penanganan acara klik untuk tombol kirim data
    document.getElementById("kirimdata").addEventListener("click", function() {
        if (validateForm(Form1) && validateForm(Form2) && validateForm(Form3) && validateForm(Form4)) {
            mergeForm(Form1);
            mergeForm(Form2);
            mergeForm(Form3);
            mergeForm(Form4);
            console.log(formdata);
            sendData(formdata);
        }
    });
});
