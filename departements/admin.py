from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# pip install django-admin-interface pour pouvoir voir le theme personnalisé
# aux couleurs de l'EPT
from admin_interface.models import Theme #pour unregister(Theme)


#enlever l'affichage de la date de naissance
class EtudiantA(admin.ModelAdmin):
    #exclude = ('date_de_naissance', )
    list_display = ('prenom', 'nom' , 'date_dinscription')
    list_filter = ('date_dinscription', )
    list_per_page=10

class ProfesseurA(admin.ModelAdmin):
    list_display = ('prenom', 'nom' , 'Chef_departement_de')
    list_filter = ('nom', )
    list_per_page=100

class MatiereA(admin.ModelAdmin):
    list_display = ('nom_matiere', 'code_matiere' , 'enseigner_par' ,'enseigner_dans')


# Register your models here.
from .models import*
admin.site.register(Etudiant , EtudiantA)
admin.site.register(Professeur , ProfesseurA)
admin.site.register(Departement)
admin.site.register(Classe)
admin.site.register(UE_matiere)
admin.site.register(Matiere , MatiereA)
admin.site.register(UserExtension)

#unregister Group , User , Theme
admin.site.unregister(Group)
admin.site.unregister(Theme)

#PERSONNALISATION
admin.site.site_header = "EPT ADMINISTRATION"
admin.site.site_title = "EPT administration"
admin.site.index_title="Site administration de l'EPT"
admin.site.empty_value_display = "*"
