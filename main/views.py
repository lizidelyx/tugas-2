from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.forms import Item
from django.http import HttpResponse
from django.core import serializers
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound



#untuk membuat login form 
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def hapus_produk_ajax(request, product_id):
    if request.method == 'DELETE':
        product = get_object_or_404(Item, pk=product_id)
        product.delete()
        return HttpResponse(status=204)  # Menyatakan penghapusan berhasil
    return HttpResponse(status=400)  # Permintaan yang tidak valid

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        if name and amount:  # Pastikan name dan amount tidak kosong
            new_product = Item(name=name, amount=amount, description=description, user=user)
            new_product.save()
            return JsonResponse({'message': 'Product created successfully'})
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_product_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def tambah_produk(request, product_id):
    try:
        produk = Item.objects.get(id=product_id)
        produk.amount += 1

        # Validasi agar jumlah produk tidak negatif
        if produk.amount < 0:
            produk.amount = 0

        produk.save()
        jumlah_item = sum([product.amount for product in Item.objects.all()])

        # Mengembalikan respons JSON yang berisi data jumlah produk yang baru
        return JsonResponse({'new_amount': produk.amount, 'new_total_item': jumlah_item})
    
    except Item.DoesNotExist:
        # Handle jika produk tidak ditemukan
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)

def kurang_produk(request, product_id):
    try:
        produk = Item.objects.get(id=product_id)
        produk.amount -= 1

        # Validasi agar jumlah produk tidak negatif
        if produk.amount < 0:
            produk.amount = 0

        produk.save()
        jumlah_item = sum([product.amount for product in Item.objects.all()])

        # Mengembalikan respons JSON yang berisi data jumlah produk yang baru
        return JsonResponse({'new_amount': produk.amount, 'new_total_item': jumlah_item})
    except Item.DoesNotExist:
        # Handle jika produk tidak ditemukan
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)


def hapus_produk(request, product_id):
    try:
        produk = Item.objects.get(id=product_id)
        produk.delete()
        # Redirect ke halaman yang sesuai setelah menghapus objek
        return redirect('main:show_main')
    except Item.DoesNotExist:
        # Handle jika produk tidak ditemukan
        return redirect('main:show_main')  # Redirect ke halaman produk setelah menghapus

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm() # membuat UserCreationForm baru dari yang sudah di-impor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #membuat dan menyimpan data dari form tersebut. 
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


    
    

@login_required(login_url='/login')
def show_main(request):
    products = Item.objects.filter(user=request.user)

    jumlah_item = sum(product.amount for product in products)

    jumlah_produk = products.count()
    last_login = request.COOKIES.get('last_login', 'Tidak ada informasi login sebelumnya')  # Menggunakan get untuk menghindari KeyError

    context = {
        'name': request.user.username,
        'products': products,
        'jumlah_produk': jumlah_produk,
        'jumlah_item': jumlah_item,
        'last_login': last_login,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)