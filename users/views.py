from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username},your account is created succesfully')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
  
    return redirect ('food:index')

@login_required
def profilepage(request):
    return render(request,'users/profile.html')
