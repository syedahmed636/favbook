from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username=username, password=password)
                if user is not None:
                        auth.login(request, user)
                        return redirect('home')
                else:
                        messages.info(request, 'Invalid Credentials..')
                        return redirect('/')

        else:
                return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=pass2, email=email)
                user.save()
                messages.info(request, 'Registered Successfully..')
                return redirect('/')
        else:
            messages.info(request, 'Password not matching..')
            return redirect('register')
    else:
        return render(request, 'register.html')