from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import EventForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

  
def event_checklist(request):
    return render(request, "event_checklist.html")
       
    
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists',
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match',
        })

      
def signout(request):
    logout(request)
    return redirect('signin')

  
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')
        
def admin(request):
    return redirect(admin.site.urls)

def create_event(request):
    if request.method == 'GET':
        return render(request, 'create_event.html', {
        'formForEvents': EventForm
        })
    else:
         try:
            form = EventForm(request.POST)
            newEvent = form.save(commit=False) #el commit=False es para que aún no lo guarde en la BD
            newEvent.save()
            return redirect("home")
         except:
             return render(request, "create_event.html", {
                 "formForEvents": EventForm,
                 'error': 'Por favor, digite valores válidos'
             })


    
