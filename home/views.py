from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from home.forms import ConnexionForm , InscriptionForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from departements.models import Etudiant
from rest_framework import generics
from departements.serializers import EtudiantSerializer


class API_objects(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class =EtudiantSerializer

# Create your views here.
def home(request):
    # recuperations des informations de la table Personne
    user_credentials = User.objects.all()
    return render(request, 'base.html' , {'user_credentials': user_credentials })

def upload(request):
    upload = ConnexionForm()
    inscription = InscriptionForm()
    if request.method == 'POST':
        inscription = InscriptionForm(request.POST, request.FILES)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            request.session['name'] = username
            request.session['password'] = password
            return redirect("/")
        else:
            return HttpResponse("""identifiants incorrects recharger la page ? <a href = "">reload</a>""")
        if inscription.is_valid():
            inscription.save()
            return HttpResponse("reussite")
        else:
            return HttpResponse("echec")
    else:
        return render(request, 'base.html', {'upload_form':upload , 'inscription':inscription})

def sign_out(request): #my logout view
    request.session.flush()
    return redirect("/")

def contacts(request): #my logout view
    upload = ConnexionForm()
    inscription = InscriptionForm()
    if request.method == 'POST':
        inscription = InscriptionForm(request.POST, request.FILES)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            request.session['name'] = username
            request.session['password'] = password
            return redirect("/")
        else:
            return HttpResponse("""identifiants incorrects recharger la page ? <a href = "">reload</a>""")
        if inscription.is_valid():
            inscription.save()
            return HttpResponse("reussite")
        else:
            return HttpResponse("echec")
    else:
            return render(request, "contacts.html" , {'upload_form':upload })

def departement_GIT(request): #my logout view
    liste_git = Etudiant.objects.filter(departement='GIT')
    upload = ConnexionForm()
    inscription = InscriptionForm()
    if request.method == 'POST':
        inscription = InscriptionForm(request.POST, request.FILES)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            request.session['name'] = username
            request.session['password'] = password
            return redirect("/")
        else:
            return HttpResponse("""identifiants incorrects recharger la page ? <a href = "">reload</a>""")
        if inscription.is_valid():
            inscription.save()
            return HttpResponse("reussite")
        else:
            return HttpResponse("echec")
    else:
        return render(request, "departement_GIT.html" , {'liste_git':liste_git , 'upload_form':upload })
