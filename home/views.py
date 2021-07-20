from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from home.forms import ConnexionForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    # recuperations des informations de la table Personne
    user_credentials = User.objects.all()
    return render(request, 'base.html' , {'user_credentials': user_credentials })

def upload(request):
    upload = ConnexionForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponse("reussite")
        else:
            return HttpResponse("echec")
    else:
        return render(request, 'base.html', {'upload_form':upload})
