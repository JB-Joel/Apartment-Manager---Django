from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateAptForm, CreateTenantForm

# Create your views here.
def home(req):
    return render(req, 'apart/home.html')#, context={})

@login_required
def dashboard(req):
    apts = Apartment.objects.filter(user=req.user)
    tenants = Tenant.objects.all()
    oqp_apts = apts.exclude(tenant=None).count()

    context = {
        'apts': apts,
        'tenants': tenants,
        'counts': {
                    'occupied':oqp_apts,
                    'empty':apts.count()-oqp_apts
                    },
    }
    return render(req, 'apart/dashboard.html', context)

@login_required
def apartDetails(req, pk):
    context = {
        'apt': Apartment.objects.get(name=pk)
    }
    return render(req, 'apart/apart_details.html', context)

@login_required
def createApt(req):
    if req.method == "POST":
        form = CreateAptForm(req.POST)
        if form.is_valid():
            new_apt = Apartment.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                rooms=form.cleaned_data['rooms'],
                bathrooms=form.cleaned_data['bathrooms'],
                kitchen=form.cleaned_data['kitchen'],
                user=req.user
                )
            # form.cleaned_data['user'] = req.user
            # form.save()
            return redirect('apart_details', new_apt.name)

    form = CreateAptForm()
    context = {
        'form': form
    }
    return render(req, 'apart/add_apart.html', context)

@login_required
def createTenant(req, pk):
    if req.method == "POST":
        form = CreateTenantForm(req.POST)
        if form.is_valid():
            apt = Apartment.objects.get(id=pk)
            Tenant.objects.create(
                name = form.cleaned_data['name'],
                dob = form.cleaned_data['dob'],
                CNI = form.cleaned_data['CNI'],
                phone = form.cleaned_data['phone'],
                entry_date = form.cleaned_data['entry_date'],
                apt = apt
                )
            return redirect('apart_details', apt.name) #use reverse here

    form = CreateTenantForm()
    context = {
        'form': form
    }
    return render(req, 'apart/add_tenant.html', context)