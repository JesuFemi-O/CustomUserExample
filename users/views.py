from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import RegistrationForm

# Create your views here.
def homeView(request):
    return render(request, 'account/home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def registration_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
    form = RegistrationForm()
    return render(request, 'account/register.html', {'form':form})