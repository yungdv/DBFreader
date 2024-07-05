from django.shortcuts import render, redirect
from .models import EquipmentType, Model, Hardware
from .forms import EquipmentTypeForm, ModelForm, HardwareForm

def home(request):
    return render(request, 'inventory/home.html')

def equipment_type_list(request):
    types = EquipmentType.objects.all()
    return render(request, 'inventory/equipment_type_list.html', {'types': types})

def equipment_type_create(request):
    if request.method == 'POST':
        form = EquipmentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_type_list')
    else:
        form = EquipmentTypeForm()
    return render(request, 'inventory/equipment_type_form.html', {'form': form})

def model_list(request):
    models = Model.objects.all()
    return render(request, 'inventory/model_list.html', {'models': models})

def model_create(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_list')
    else:
        form = ModelForm()
    return render(request, 'inventory/model_form.html', {'form': form})

def hardware_list(request):
    hardware = Hardware.objects.all()
    return render(request, 'inventory/hardware_list.html', {'hardware': hardware})

def hardware_create(request):
    if request.method == 'POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hardware_list')
    else:
        form = HardwareForm()
    return render(request, 'inventory/hardware_form.html', {'form': form})
