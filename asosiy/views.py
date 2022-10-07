from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *

def all_plans(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Plan.objects.create(
                sarlavha = request.POST.get('s'),
                batafsil = request.POST.get('b'),
                sana = request.POST.get('sana'),
                status = request.POST.get('st'),
                student = Student.objects.get(user=request.user)
            )
            return redirect('/plans/')
        data = {
            'plans':Plan.objects.filter(student__user=request.user)
        }
        return render(request, 'todo.html', data)
    else:
        return redirect('/')

def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/plans/')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        u = User.objects.create_user(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        Student.objects.create(
            fullname = request.POST.get('fl'),
            guruh = request.POST.get('g'),
            st_raqam = request.POST.get('st'),
            tel = request.POST.get('t'),
            user = u
        )
        return redirect('/')
    return render(request, 'register.html')



