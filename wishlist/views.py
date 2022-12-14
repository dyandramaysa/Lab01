from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
# Tutorial Lab 03
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Manambahkan Cookies
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

# Create your views here.
data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Nadira',
}

@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Nadira Maysa Dyandra',
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist.html", context)

# Lab 5
@login_required(login_url='/wishlist/login/')
def show_ajax(request):
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Nadira Maysa Dyandra',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist_ajax.html", context)

def add_wishlist_ajax(request):
    if request.method == 'POST':
        nama_barang = request.POST.get('nama_barang')
        harga_barang = request.POST.get('harga_barang')
        deskripsi = request.POST.get('deskripsi')
        item = BarangWishlist(nama_barang=nama_barang, harga_barang=harga_barang, deskripsi=deskripsi)
        item.save()
        return JsonResponse({"instance": "Proyek Dibuat"}, status=200)

# Tutorial Lab02
data = BarangWishlist.objects.all()
def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Tutorial Lab 03
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response