from django.db import models

# Create your models here.
# ici on utilise la classe User de django qu'on va expandre pour gerer nos utilisateurs




# Create your models here.
class Utilisateur(models.Model):
    class Meta:
        ordering = ('nom',)
    prenom = models.CharField(max_length = 200)
    nom = models.CharField(max_length = 200)
    mail = models.EmailField(max_length=100 , primary_key=True)
    def __str__(self):
        return self.prenom

class Departement(models.Model):
    class Meta:
        pass

    class Choix1(models.TextChoices):
        aucun = 'AUCUN'
        git = 'GIT'
        gem = 'GEM'
        aero = 'AERO'
        civil = 'GC'

    nom_departement = models.TextField(choices=Choix1.choices , primary_key=True)
    mail_departement = models.EmailField(max_length=100)
    numero_departement = models.TextField(max_length=100)
    description_dept = models.TextField(max_length=1000)
    def __str__(self):
        return self.nom_departement

    def show_desc(self):
        return self.description_dept[:50]

class Etudiant(Utilisateur):
    class Meta:
        pass

    date_de_naissance = models.DateField(null=True)
    date_dinscription = models.DateField()
    lieu_de_naissance = models.CharField(max_length = 200)


    appartient = models.ManyToManyField('Classe')
    departement = models.ManyToManyField('Departement',default='GIT')


class Professeur(Utilisateur):
    class Meta:
        pass

    contact_prof = models.TextField(max_length=100)
    date_d_adhesion = models.DateField()
    class Choix(models.TextChoices):
        aucun = 'AUCUN'
        git = 'GIT'
        gem = 'GEM'
        aero = 'AERO'
        civil = 'GC'

    enseigner_dans = models.ManyToManyField('Departement')
    Chef_departement_de = models.TextField(choices=Choix.choices , default=Choix.aucun)

    def __str__(self):
        return self.prenom+' '+self.nom


class Classe(models.Model):
    class Meta:
        pass

    nom_classe = models.TextField(max_length=100  , primary_key=True)
    description_classe = models.TextField(max_length=1000)

    def __str__(self):
        return self.nom_classe

    def show_desc(self):
        return self.description_classe[:50]




class Matiere(models.Model):
    class Meta:
        pass

    nom_matiere = models.TextField(max_length=300)
    code_matiere = models.TextField(max_length=100  , primary_key=True)
    coef_matiere =  models.IntegerField()
    credit_matiere = models.IntegerField()
    quota_horaire = models.IntegerField()
    description_matiere = models.TextField(max_length=1000)
    enseigner_par = models.OneToOneField('Professeur' , on_delete=models.PROTECT)
    enseigner_dans = models.OneToOneField('Classe'  , on_delete=models.PROTECT)

    appartenir = models.ForeignKey('UE_matiere', on_delete=models.PROTECT)
    def __str__(self):
        return self.nom_matiere

class UE_matiere(models.Model):
    class Meta:
        pass

    nom_UE = models.TextField(max_length=100)
    code_UE = models.IntegerField()
    credit_UE = models.IntegerField()

    concerner = models.ForeignKey('Classe', on_delete=models.PROTECT)
    def __str__(self):
        return self.nom_UE

    def coef_UE(self, ):
        pass

    def credit_UE(self, ):
        pass
