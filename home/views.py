from django.shortcuts import render

# Create your views here.
def home(request):
    # recuperations des informations de la table Personne
    return render(request, 'base.html')
