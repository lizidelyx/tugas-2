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
   a. Membuat input form untuk menambahkan objek model pada app sebelumnya.
       Saya membuat file forms.py yang berfungsi sebagai struktur form yg dapat menerima data baru. Di dalam forms.py terdapat dungsi ProductForm yang berisi variabel model yang merupakan objek produk yang akan diisi ke form. Kemudian terdapat field yang menunjukkan field dari model product. 
       Selanjutnya pada file views.py saya import fungsi ProductForm yang ada pada forms.py kemudian saya membuat fungsi create_product dengan parameter request pada views.py. Di fungsi create_product saya menggunakan request.Post untuk membuat productform baru yang kemudian input dari usr akan dmasukkan di QueryDict. lalu saya melakukan pemanggilan return HttpResponseRedirect(reverse('main:show_main')) agar tampilan kembali ke show.main saat data sudah berhasil di simpan di form.
       Pada fungsi show_main di views.py saya menambahkan variabel products = Product.objects.all() agar seluruh object yang tersimpan ( ditambah ke form ) dapat diambil dan ditampilkan ke user. lalu pada bagian context saya tambahkan key products dengan valuenya products ( objek yang sudah disimpan tadi )
       lalu pada urls.py saya import fungsi create_product dari views.py dan menambah path baru pada URL pattern : path('create-product', create_product, name='create_product') agar path create_product bisa di akses oleh user.
       Saya menambahkan file create_product.html yang merupakan tampilan web untuk menambahkan/menginput data.
       Lalu pada main.html saya memodifikasinya agar dapat meampilkan info data-data yang telah di tambahkan oleh user.
   
    b. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

       Untuk melihat objek dalam format JSON dan XML saya membuat fungsi baru di views.py. Saya membuat fungsi show_xml dan show_json yang masing-masing memiliki variabel data yang mengambil info product dengan Product.objects.all(). Selanjutnya keduanya sama-sama me return tampilan data tersimpan dengan format JSON dan XML. perbedaannya ada pada :  JSON=HttpResponse(serializers.serialize("json", data), content_type="application/json")
XML=return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    lalu saya meambahkan path baru ( path untuk JSON dan XML ) di URLs pattern pada urls.py agar tampilan web XML dan JSON dapat diakses oleh pengguna.

   Untuk XML by ID dan JSON by ID saya menambahkan fungsi show_xml_by_id dan show_json_by_id yang memiliki parameter request dan id di file views.py dengan variabel data mengambil info product yang tersimpan berdasarkan id. Return dari kedua fungsi ini hampir sama dengan return di show_xml dan show_JSON hanya saja variabel data yang diambil sudah berdasarkan id product.
   Selanjutnya saya menambahkan url baru di Url pattern pada urls.py agar pengguna dapat mengakses xml by id dan JSOn by id dengan menambahkan :
   ...
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
...


Screenshoot : 

<img width="960" alt="Screenshot 2023-09-20 024149" src="https://github.com/lizidelyx/tugas-2/assets/121842969/06d27e44-cff1-4558-b317-c6cb4b248310">
<img width="958" alt="Screenshot 2023-09-20 024314" src="https://github.com/lizidelyx/tugas-2/assets/121842969/4799e12f-0988-42d4-9963-7753a97ef714"><img width="960" alt="Screenshot 2023-09-20 024206" src="https://github.com/lizidelyx/tugas-2/assets/121842969/8361f674-b0e3-4863-9585-c90d530f8645">
<img width="960" alt="Screenshot 2023-09-20 024218" src="https://github.com/lizidelyx/tugas-2/assets/121842969/be5bca02-dfc0-4109-a528-7f2d6ca86cc1">
<img width="960" alt="Screenshot 2023-09-20 024229" src="https://github.com/lizidelyx/tugas-2/assets/121842969/15db1387-9a79-4543-b5e2-39c8846a8ff8">



Refrensi : 
- Perbedaan metode POST dan GET. https://www.dumetschool.com/blog/Perbedaan-Metode-POST-Dan-GET
- Kotakode.com | Komunitas Developer Indonesia. https://kotakode.com/blogs/2718/Perbedaan-Method-GET-dan-POST
- JSON Adalah Format Data yang Populer, Kenapa? Midtrans. Published September 15, 2023. https://midtrans.com/id/blog/json-format
- Grill M. HTML Vs JSON: What's The Difference? - BSharp Tech. BSharp Tech. Published online August 18, 2023. https://bsharptech-com-au.translate.goog/html-vs-json-whats-the-difference/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc
