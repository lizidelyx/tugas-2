1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
     Fitur form yang disediakan django untuk memudahkan proses pembuatan akun dalam suatu aplikasi web.
   Kelebihan :
   a. Mudah digunakan
   b. Memiliki fitur validasi otomatis dimana akan mencocokan inputan pengguna dengan data yang disimpan.
   Kekurangan :
   a. Perlu menyesuaikan sendiri tampilan form jika ingin membuat form register yang lebih complex
   

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
   Autentikasi : Proses verifikasi/validasi suatu identitas yang sudah terdaftar sebelumnya.
   Otorisasi : Proses menentukan apakah pengguna yang melakukan izin untuk masuk memiliki kewenangan untuk mengakses data

   Autentikasi dan Otorisasi tentu saja penting untuk menajaga keamanan dan privasi pengguna. Selain itu dengan adanya    autentikasi dan otorisasi kita bisa menentukan siapa saja yang bisa mengakses apa.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   cookies merupakan suatu file yang ditempatkan pada komputer pengguna saat pengguna tersebut sedang membuka suatu website. Cookies biasanya digunakan untuk menyimpan identitas pengguna, menyimpan preferensi pengguna, melacak aktivitas pengguna dan melacak sesi login/logout pengguna.
   Pada django terdapat beberapa fitur untuk menggunakan cookies contohnya :
   
  
from django.contrib.sessions.models import Session --> untuk mengimpor modul sesi Django

def set_session_data(request):
    request.session['username'] = 'pengguna123' --> untuk menyimpan data user

def get_session_data(request):
    username = request.session.get('username', 'Tidak ada username') --> untuk mengakses data sesi user
    return f'Nama Pengguna: {username}'

   
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
  Penggunaan cookies ini ada yang aman ada yang tidak. Jika digunakan dengan baik, tentu pengimplementasian cookies ini aman dan sangat berguna. Resiko-resiko yang harus dihadapi akan penggunaan cookies :
  a. Pencurian data
b. Kebocoran informasi
c. Pelanggaran privasi data
d. Penyisipan skrip berbahaya untuk suatu halaman dalam web

7. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara setp-by-step

   # Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
   a. mengimport import redirect, UserCreationForm, dan messages pada views.py :
      from django.shortcuts import redirect
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages
   b. Membuat fungsi register yang akan me return register.html dengan isi fungsi sebagai berikut :
       def register(request):
        form = UserCreationForm()
    
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
   c. Membuat berkas html yang meminta input dari user dengan isi sebagai berikut :
   {% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}

d. Pada urls.py import fungsi register dari views.py yang ada di berkas main. lalu menambahkan path register pada url_pattern 

e. Untuk membuat fungsi login dan logout, tambahkan import authenticate untuk login dan logout pada views.py : 
    from django.contrib.auth import authenticate, login, logout

f. Menambahkan fungsi login_user dan logout user pada views.py

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

  def logout_user(request):
    logout(request)
    return redirect('main:login')

    g.Untuk login, selanjutnya dibuat file html dengan nama login,html dengan isi sebagai berikut :
    {% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}

untuk logout ditambahkan : 
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...

pada main.html

h. selanjutnya import dungsi login_user dan logout pada urls.py dan mengisi bagian urlspattern dengan login dan logout agar program dapat mengakses web untuk login dan logout


# Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
  Setelah poin pertama diselesaikan, kita dapat langsung register untuk membuat suatu akun. Untuk membuat dua akun pengguna bisa melakukan register sebanyak 2x 

# Menghubungkan model Item dengan User.

  a. Imprort User pada models.py :
    from django.contrib.auth.models import User
  b. pada class product yang ada di models.py tambahkan user : 
    class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)

    c. modifikasi codingan pada fungsi create_product : 
      def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))

     d. modifikasi fungsi show_main dengan menambahkan key 'name' dan request.user.username sebagai valuenya : 

     def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,

        e. selanjutnya melakukan migration agar program dapat menerima pengubahan pada models.
  


# Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
  a. IMport datetime pada view.pu
  b.  Pada fungsi login_user modifikasi codingan dengan menambahkan codingan berikut pada if user not None : 
    if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response

  c.Pada fungsi showmain, ditambahkan key 'last_login' dengan value : request.COOKIES['last_login']
  d. pada main html ditambahkan codingan berikut agar value dari last_login dapat ditampilkan kepada pengguna  :
  <h5>Sesi terakhir login: {{ last_login }}</h5>
  

# Tambahkan tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
  a. Pada bagian main.html saya menambahkan code untuk membuat button "+" dan "-" yang menghubungkan button dengan penambahan data/pengurangan data : 
  <td>
                    <span id="amount_{{ product.id }}">{{ product.amount }}</span>
                    <button class="btn-increment" data-product-id="{{ product.id }}" data-increment="1">+</button>
                    <button class="btn-decrement" data-product-id="{{ product.id }}" data-increment="-1">-</button>

    b. di bawahnya akan ada fungsi yang menerima action saat button di tekan dengan code sebagai berikut  : 
      document.addEventListener('DOMContentLoaded', function () {
            const incrementButtons = document.querySelectorAll('.btn-increment');
            const decrementButtons = document.querySelectorAll('.btn-decrement');
     incrementButtons.forEach(button => {
                button.addEventListener('click', function () {
                    const productId = this.getAttribute('data-product-id');
                    const incrementValue = parseInt(this.getAttribute('data-increment'));
                    const amountElement = document.getElementById(`amount_${productId}`);
                    const currentAmount = parseInt(amountElement.innerText);
                    const newAmount = currentAmount + incrementValue;
    
                    amountElement.innerText = newAmount;
    
                   
                });
            });
    
            decrementButtons.forEach(button => {
                button.addEventListener('click', function () {
                    const productId = this.getAttribute('data-product-id');
                    const incrementValue = parseInt(this.getAttribute('data-increment'));
                    const amountElement = document.getElementById(`amount_${productId}`);
                    const currentAmount = parseInt(amountElement.innerText);
                    const newAmount = currentAmount + incrementValue;
    
                    amountElement.innerText = newAmount;

    
                </td>

# Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.
a. menambahkan tombol hapus di sebelah description tiap item dengan codingan sebagai berikut :

<form method="post" action="{% url 'main:hapus_produk' product.id %}">
                        {% csrf_token %}
                        <button type="submit">Hapus</button>
                    </form>
  b. Membuat fungsi hapus_produk pada views.py guna menghapus item yang disimpan : 

  def hapus_produk(request, product_id):
    try:
        produk = Item.objects.get(id=product_id)
        produk.delete()
        # Redirect ke halaman yang sesuai setelah menghapus objek
        return redirect('main:show_main')
    except Item.DoesNotExist:
        # Handle jika produk tidak ditemukan
        return redirect('main:show_main')  # Redirect ke halaman produk setelah menghapus
                    


