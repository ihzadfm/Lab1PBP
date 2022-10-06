import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from wishlist.models import BarangWishlist
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Ihza Dafa',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "wishlist.html", context)

@login_required(login_url='/wishlist/login/')
def show_wishlist_ajax(request):
    context = {
        'last_login': request.COOKIES['last_login'],
    }
    
    return render(request, "wishlist_ajax.html", context)

def submit_wishlist(request):
    if request.method == 'POST':
        nama_barang = request.POST['nama_barang']
        deskripsi = request.POST['deskripsi']
        harga_barang = request.POST['harga_barang']
        wishlist_instance = BarangWishlist(nama_barang=nama_barang, deskripsi=deskripsi, harga_barang=harga_barang)
        wishlist_instance.save()
        data = {
            "message": 'Successfully submitted'
        }
        json_object = json.dumps(data, indent = 4) 

        return JsonResponse(json.loads(json_object))
    return render(request, 'generate_wishlist.html')
        

def show_xml(request):
    data = BarangWishlist.objects.all()
    
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_json(request):
    data = BarangWishlist.objects.all()
    
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response