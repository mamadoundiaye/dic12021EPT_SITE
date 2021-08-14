from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from home.forms import ConnexionForm , InscriptionForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from departements.models import Etudiant
from rest_framework import generics
from departements.serializers import EtudiantSerializer
from django.utils.translation import gettext_lazy, gettext
from django.utils import translation
from django.conf import settings


class API_objects(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class =EtudiantSerializer

# Create your views here.

def firstvisit(request):
    request.session.flush()
    return redirect('/home')

def home(request):
    upload = ConnexionForm()
    inscription = InscriptionForm()
    if request.method == 'POST' :
        if len(request.POST) == 2 :
            response = HttpResponseRedirect('/home')
            response.set_cookie('django_language', request.POST['langue'])
            return response
        elif len(request.POST) == 3:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                request.session['name'] = username
                request.session['password'] = password
                return redirect(request.path_info)
            elif user is None or user.DoesNotExist:
                return HttpResponse("""identifiants incorrects recharger la page ? <a href = "">reload</a>""")
        else :
            inscription = InscriptionForm(request.POST, request.FILES)
            if inscription.is_valid() :
                user = inscription.save()
                user.set_password(request.POST['password'])
                user.save()
                return redirect(request.path_info)
            else:
                return HttpResponse("""une erreur est survenu : username deja utilise ou mdp ne correspondant pas  recharger la page ? <a href = "">reload</a>""")
    else:
        return render(request, 'base.html', {'upload_form':upload , 'inscription':inscription})

def sign_out(request):
    request.session.flush()
    return redirect('/home')

def contacts(request): 
    upload = ConnexionForm()
    inscription = InscriptionForm()
    if request.method == 'POST' :
        if len(request.POST) == 2 :
            response = HttpResponseRedirect('/contacts')
            response.set_cookie('django_language', request.POST['langue'])
            return response
        elif len(request.POST) == 3:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                request.session['name'] = username
                request.session['password'] = password
                return redirect(request.path_info)
            elif user is None or user.DoesNotExist:
                return HttpResponse("""identifiants incorrects recharger la page ? <a href = "">reload</a>""")
        else :
            inscription = InscriptionForm(request.POST, request.FILES)
            if inscription.is_valid() :
                user = inscription.save()
                user.set_password(request.POST['password'])
                user.save()
                return redirect(request.path_info)
            else:
                return HttpResponse("""une erreur est survenu : username deja utilise ou mdp ne correspondant pas  recharger la page ? <a href = "">reload</a>""")
    else:
            return render(request, "contacts.html" , {'upload_form':upload , 'inscription':inscription})

def departement(request , dep_num): #my logout view
    liste_git = Etudiant.objects.filter(departement=dep_num)
    upload = ConnexionForm()
    inscription = InscriptionForm()
    if request.method == 'POST' :
        if len(request.POST) == 2 :
            response = HttpResponseRedirect('/departement/GIT')
            response.set_cookie('django_language', request.POST['langue'])
            return response
        elif len(request.POST) == 3:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                request.session['name'] = username
                request.session['password'] = password
                return redirect(request.path_info)
            elif user is None or user.DoesNotExist:
                return HttpResponse("""identifiants incorrects recharger la page ? <a href = "">reload</a>""")
        else :
            inscription = InscriptionForm(request.POST, request.FILES)
            if inscription.is_valid() :
                user = inscription.save()
                user.set_password(request.POST['password'])
                user.save()
                return redirect(request.path_info)
            else:
                return HttpResponse("""une erreur est survenu : username deja utilise ou mdp ne correspondant pas  recharger la page ? <a href = "">reload</a>""")
    else:
        return render(request, "departement.html" , {'liste_git':liste_git , 'upload_form':upload ,'nom_departement':dep_num , 'inscription':inscription})
