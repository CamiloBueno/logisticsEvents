from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# In here, we must create the HTMLs
# Create your views here.

def signup(request):
    return render(request, 'signup.html', {
        "form": UserCreationForm
    })

def event_checklist(request):
    
    return render(request, "event_checklist.html")
       
def home(request):
    return render(request, "home.html",
