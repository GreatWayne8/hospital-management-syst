from django.shortcuts import render,redirect
from .form import PatientForm
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else: 
        form = PatientForm()
    return render(request, 'patient/register.html',{'form':form})