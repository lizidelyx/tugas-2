1. Apa perbedaan antara form POST dan form GET dalam Django?
    <POST>
    a. Data dan nilai dikirim langsung ke action tanpa melalui URL ( Data/nilai --> action )
    b. Data yang dikirim tidak terbatas
    c. Lebih aman untuk mengirim data yang sensitif ( contohnya password ) karena lebih aman.

    <GET>
    a. Data dan nilai dikirim/ditampilkan terlebih dahulu di URL, setelah itu dikirim ke action ( Data/nilai --> url --> action )
    b. Data yang dikirim tidak bisa lebih dari 2047 karakter.
    c. Tidak aman untuk mengirim data yang sensitif, sebaiknya gunakan GET untuk mengirim data yang bersifat umum.

    

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    <XML>
    a. Menggunakan elemen dan atribut dalam mengorganisir datanya
    b. XML merupakan bahasa markup yang bertujuan untuk mendefinisikan struktur data yang lebih kompleks dan khusus.
    c. Digunakan untuk pertukaran data dalam berbagai format misalnya SVG

    <JSON>
    a. Sintaksisnya berbentuk key-value (mirip objek javascript)
    b. Tujuannya untuk menyimpan, mengirim, dan menerima data dalam format yang ringkas sehingga mudah dibaca oleh manusia dan mesin.
    c. Digunakan untuk pertukaran data melalui API web atau aplikasi lain yang membutuhkan pertukaran data yang terstruktur

    <HTML>
    a.Memiliki elemen-elemen khusus yang digunakan untuk menampilkan teks, gambar, tautan, dan berbagai elemen lainnya di suatu web
    b. Fungsi utamanya adalah untuk membangun web
    c. Digunakan untuk pembangunan tampilan web

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    a. Formatnya lebih sederhana
    b. Bayak platform yang mendukung penggunaan JSON
    c. Banyak API web modern menggunakan JSON sebagai format pertukaran data standar. 
    d. Didasari oleh bahasa JavaScript
    e. Mudah dibaca oleh manusia
    f. Mudah dibaca oleh mesin
    g. Proses pertukaran datanya cepat

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


Refrensi : 
- Perbedaan metode POST dan GET. https://www.dumetschool.com/blog/Perbedaan-Metode-POST-Dan-GET
- Kotakode.com | Komunitas Developer Indonesia. https://kotakode.com/blogs/2718/Perbedaan-Method-GET-dan-POST
- JSON Adalah Format Data yang Populer, Kenapa? Midtrans. Published September 15, 2023. https://midtrans.com/id/blog/json-format
- Grill M. HTML Vs JSON: What's The Difference? - BSharp Tech. BSharp Tech. Published online August 18, 2023. https://bsharptech-com-au.translate.goog/html-vs-json-whats-the-difference/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc