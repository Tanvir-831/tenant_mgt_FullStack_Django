from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Building, Flat
from .forms import BuildingForm, FlatForm, FlatUpdateForm

# Create your views here.

def home(request):
    flats = Flat.objects.all()

    return render(request, 'tenants/home.html', {'flats': flats})



def show_buildings(request):
    buildings = Building.objects.all()

    return render(request, 'tenants/show_buildings.html', {'buildings': buildings})


def show_flats(request, id):
    flats = Flat.objects.filter(building=id)

    building = Building.objects.get(id=id)

    return render(request, 'tenants/show_flats.html', {'flats': flats, 'building': building})

def add_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)

        if form.is_valid():
            building = form.save(commit=False)
            building.owner = request.user
            building.save()

            return redirect('show-buildings')
    else:
        form = BuildingForm()

    return render(request, 'tenants/add_building.html', {'form': form})


def add_flat(request):
    if request.method == 'POST':
        form = FlatForm(request.POST)

        if form.is_valid():
            flat = form.save(commit=False)
            flat.owner = request.user
            flat.save()

            return redirect('home')
    else:
        form = FlatForm()

    return render(request, 'tenants/add_flat.html', {'form': form})
    
    

    

def my_flats(request):
    flats = Flat.objects.filter(owner=request.user)

    return render(request, 'tenants/my_flats.html', {'flats': flats})

def dashboard(request):
    flats = Flat.objects.all()
    return render(request, 'tenants/dashboard.html', {'flats': flats})

def userlist(request):
    users = User.objects.all()
    return render(request, 'tenants/user_list.html', {'users': users})


def get_rent(request, id):
    flat = Flat.objects.get(id=id)

    flat.tenant = request.user
    flat.save()

    return redirect('home')


def edit_flat(request, id):
    flat = Flat.objects.get(id=id)

    if request.method == 'POST':
        form = FlatUpdateForm(request.POST, instance=flat)

        if form.is_valid():
            form.save()

            return redirect('my-flats')
    else:
        form = FlatUpdateForm(instance=flat)

    return render(request, 'tenants/edit_flat.html', {'form': form})


def delete_flat(request, id):
    flat = Flat.objects.get(id=id)
    flat.delete()

    return redirect('my-flats')