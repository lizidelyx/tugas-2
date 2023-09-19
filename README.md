Adaptable : ( disable )

Nama : Alizza Deli Satria 
NPM 2206082423
Kelas : PBP B


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - <Membuat sebuah proyek Django baru.> Buat sebuah direktori baru yang akan dijadikan tempat membuat project django, selanjutnya masuk ke dalam Virtual Environtment ( via command promt ) dan mulai membuat project django. Dalam membuat project ini bisa dengan menginput "django-admin startproject <nama project>" di cmd. Setelau itu base directory dan project directory akan otomatis muncul di dalam direktori yang kita buat di awal. Setelah itu server django sudah bisa dijalankan dengan input "python manage.py runserver" di cmd.
    - <Membuat aplikasi dengan nama main pada proyek tersebut.> dilakukan dengan cara menginput python manage.py startapp main di terminal.
    - <Melakukan routing pada proyek agar dapat menjalankan aplikasi main>mengisi INSTALLED_APPS = 
    'main' pada settings.py di direktori proyek. Membuat file urls.py di dalam direktori app main yang kemudian diisi variabel app_name dan Url pattern yang berfungsi untuk mengarahkan server ke view yang kemudian dihubungkan ke html yang akan ditampilkan ke pengguna.
    - <Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.> untuk memuat model dengan atribut yang sudah ditentukan isi file models.py dengan : name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    - <Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu> 
    pada view.py di direktori app : 
        from django.shortcuts import render

        def show_main(request):
            context = {
                'app_name': 'main', //nama app
                'name': 'Alizza Deli Satria', //nama saya dan kelas saya
                'class': 'PBP B'
            }

            return render(request, "main.html", context) //pemanggilan main.html dengan context yang sudah diatur diatas

    pada main.html :
    <h1>Itemopia Page</h1>

    <h5>App name: </h5>
    <p>{{ app_name }}<p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p> //akan menampilkan nama app, nama saya dan kelas saya kepada pengguna sesuai yang sudah diatur di view.py

- <Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.>
    isi urls.py : 
    from django.urls import path
    from main.views import show_main //import show_main dari views agar bsia di routing di urls.py

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'), //akan memetakan server ke view.py, di view.py akan dipetakan ke main.html
    ]


    
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    <Client> -(melakukan request)-> <urls.py> (pencocokan url pattern) --> <views.py> -(Queryset)-> <views.py> --> <Template ( html )> --> <client>

    Broser akan mengirimkan link ( request client ) kepada server ( django project server yang berjalan), kemudian  server akan menuju ke urls.py dan link tdi dicocokkan pada url pattern. jika ada yang cocok, server akan mengeluarkan suatu method yang ada di views.py. Jika membutuhkan database, maka sebelum ke views.py server akan menuju ke models untuk mengambil data, lalu kembali ke views, lalu method di views.py akan mengarahkan ke template dimana ada file html disana yang akhirnya menjadi output untuk client.
    
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environtment ini penting digunakan untuk <Isolasi Proyek> & <Manajemen Dependensi> yang memungkinkan kita bekerja pada proyek yang memiliki dependensi yang berbeda.Dependensi proyek itu akan dijalankan secara terpisah sehingga tidak terjadi tabrakan antar versi dependensi yang berbeda. 

    Membuat aplikasi web berbasis Django tanpa virtual environtment mungkin bisa dilakukan, tetapi sangat tidak dianjurkan karena tidak aman.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    <MVC (Model - View - Controller)> = 
        - Model = bertanggung jawab atas logika bisnis aplikasi serta mengelola data.
        - View  = bertanggung jawab menampilkan data kepada pengguna dan menangani intruksi dari pengguna.
        - Controller = menghubungkan model dan view dengan satu atau lebih controller

    <MVT (Model - View - Template)> =
        - Model = bertanggung jawab atas logika bisnis aplikasi serta mengelola data.
        - View  = bertanggung jawab menampilkan data kepada pengguna. Dalam django berbasis MVT, peran view lebih kompleks karena view juga mengendalikan logika bisnis tertentu
        - Template = Mengatur bagaimana data dari model atau view ditampilkan kepada pengguna

    <MVVM (Model-View-ViewModel)> =
        - Model = bertanggung jawab atas logika bisnis aplikasi serta mengelola data.
        - View  = bertanggung jawab menampilkan data kepada pengguna tanpa memiliki logika bisnis aplikasi
        - ViewModel = lapisan pemisah atau perantara antara View dan Model.

refrensi : 
Dang AT. MVC vs MVP vs MVVM - Level Up Coding. Medium. https://levelup.gitconnected.com/mvc-vs-mvp-vs-mvvm-35e0d4b933b4. Published December 16, 2021.
