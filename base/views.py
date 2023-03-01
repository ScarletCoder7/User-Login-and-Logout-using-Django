from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import login

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password = password)  #user = authenticate(username='emily', password='@1234567@')
        if user is not None:
            login(request, user)
            return redirect("/") #redirecting to the home page
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
