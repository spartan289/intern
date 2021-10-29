from django.contrib.auth.models import UserManager
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import User_detail
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        password1 = request.POST['password1']
        if password != password1:
            return render(request, 'accounts/register.html', {'message': 'Password not match'})
        print(username,email,password,address)
        if User_detail.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'message': 'Username already exists'})
        elif User_detail.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {'message': 'Email already exists'})
        else:
            user = User_detail.objects.create(username=username,email=email,password=password,address=address)
            user.save()
        return redirect('login')
    return render(request, 'accounts/register.html')
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        if User_detail.objects.filter(username=username,password=password).exists():
            request.session['username']=username
            request.session['password']=password
            request.session.set_expiry(300)
            return redirect('index')
        else:
            return render(request,'accounts/login.html',{'message':'Username or password is incorrect'})
    else:
        return render(request,'accounts/login.html')
        
def index(request):
    try:
        username = request.session['username']
        password = request.session['password']
    except:
        return redirect('login')
    
    if request.method=='POST':
        username1 = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']

        user = User_detail.objects.filter(username=username, password=password)
        if user.exists():
            user.update(username=username1, email=email, address=address)
            request.session['username']=username1
            users = User_detail.objects.filter(username=username1, password=password).values()
            print(users)
            return render(request,'accounts/index.html',{'users':users,'username':username1})

    users = User_detail.objects.filter(username=username,password=password).values()
    print(users)

    return render(request,'accounts/index.html',{'users':users,'username':username})
def logout(request):
    try:
        del request.session['username']
        del request.session['password']
    except:
        pass
    return redirect('login')
def main(request):
    return render(request,'main.html')
def delete(request):
    try:
        username = request.session['username']
        password = request.session['password']
    except:
        return redirect('login')
    user = User_detail.objects.filter(username=username, password=password)
    if user.exists():
        user.delete()
        return redirect('main')