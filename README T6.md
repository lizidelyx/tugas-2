    1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
            Synchronous Programming (Sequential):
                Pada pemrograman sinkron, operasi-operasi dieksekusi secara berurutan atau sekuensial. Artinya, setiap operasi harus menunggu operasi sebelumnya selesai sebelum dapat dijalankan.
                Ini dapat menyebabkan aplikasi menjadi lambat ketika ada operasi yang memakan waktu, seperti mengambil data dari database atau mengunduh data dari internet.
                Dalam pemrograman berbasis thread, ini juga bisa menyebabkan blokir atau "freeze" dalam aplikasi ketika operasi memakan waktu lama.

        Asynchronous Programming (Non-Blocking):
            Dalam pemrograman asinkron, operasi-operasi dapat dieksekusi secara bersamaan tanpa harus menunggu operasi sebelumnya selesai.
            Ini membuat aplikasi menjadi lebih responsif dan dapat menangani tugas-tugas yang memakan waktu tanpa menghentikan aplikasi.
            Biasanya digunakan dalam pemrograman berbasis event, di mana program menanggapi peristiwa atau event, dan operasi-operasi tertentu akan dieksekusi hanya ketika event yang sesuai terjadi.
    
    2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
        Paradigma event-driven programming adalah pendekatan pemrograman di mana program berfungsi dengan menanggapi event atau peristiwa yang terjadi. Dalam hal ini, program akan menjalankan kode tertentu ketika event tertentu terjadi. Contoh penerapannya pada tugas ini adalah:

    3. Dalam tugas yang Anda sebutkan, paradigma event-driven programming digunakan dalam mengelola tombol-tombol seperti "Add Product by AJAX" dan tombol-tombol lainnya. Ketika tombol ini diklik, sebuah event "click" terjadi, dan program merespons event ini dengan menjalankan kode yang ditentukan, seperti mengirim permintaan AJAX atau melakukan tindakan tertentu.
    Jelaskan penerapan asynchronous programming pada AJAX.
        AJAX (Asynchronous JavaScript and XML) didasarkan pada pemrograman asinkron.
        Ketika Anda membuat permintaan AJAX, Anda tidak perlu menunggu permintaan selesai. Sebaliknya, Anda menentukan callback function yang akan dipanggil ketika permintaan selesai atau ketika data tersedia.
        Ini memungkinkan aplikasi untuk tetap merespons pengguna, bahkan saat melakukan operasi seperti mengambil data dari server.
        Penerapannya terlihat dalam contoh kode JavaScript yang telah Anda berikan, di mana Anda menggunakan fetch untuk mengirim permintaan AJAX dan kemudian menentukan tindakan yang akan diambil ketika permintaan selesai dalam blok .then(). Ini adalah contoh tipikal dari pemrograman asinkron dalam AJAX.
    
    4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
        Fetch API adalah pilihan terbaik untuk pengembangan web modern dengan JavaScript yang ringan, promise-based, dan dukungan fitur terbaru.

        jQuery lebih cocok untuk dukungan lintas browser yang luas, mudah digunakan, dan dilengkapi dengan banyak utilitas bawaan

    5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).