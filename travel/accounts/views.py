from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first']
        last_name = request.POST['last']
        username = request.POST['user']
        password1 = request.POST['pwd1']
        password2 = request.POST['pwd2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,     password=password1, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password incorrect")
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pwd']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

