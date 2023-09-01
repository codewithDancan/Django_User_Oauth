from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='signin')
def home(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('signin')
    return render(request, 'portal/home.html')


@login_required(login_url='signin')
def accordion(request):
    return render(request, 'portal/accordion.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('signin')

    return render(request, 'portal/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                messages.success(request, 'account created successfully')
                return redirect('signin')
        else:
            messages.error(request, 'Password do not match')
            return redirect('signup')

    return render(request, 'portal/signup.html')


@login_required(login_url='signin')
def logout(request):
    return render(request, 'portal/index.html')
