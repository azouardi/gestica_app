import uuid
from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Nationality(models.Model):
    code_nationality=models.CharField(max_length=3,primary_key=True, verbose_name="Code Pays")
    nationality = models.CharField(max_length=50, verbose_name="Nationalité", null=False, unique=True)
    history = HistoricalRecords()

    def __str__(self):
        """return the name of Nationalité"""
        return self.nationality

class Country(models.Model):
    code_country=models.CharField(max_length=3, primary_key=True, verbose_name="Code Nationalité")
    country = models.CharField(max_length=50, verbose_name="Pays", null=False, unique=True)
    history = HistoricalRecords()

    def __str__(self):
        """return the name of Pays"""
        return self.country

class LegalForm(models.Model):
    code_lf=models.IntegerField(primary_key=True, verbose_name="Code FJ")
    lf_name = models.CharField(verbose_name="Sigle", max_length=20, null=False, unique=True)
    full_lf_name = models.CharField(verbose_name="Forme Juridique", max_length = 300, null=False)
    history = HistoricalRecords()
    
    def __str__(self):
        """return the name of forme Juridique"""
        return self.lf_name
  
class Currency(models.Model):
    currency_code = models.CharField(max_length=3,null=False, unique=True, verbose_name="Code Devise", primary_key=True)
    currency = models.CharField(max_length=50, null=False, unique=True, verbose_name="Devise et Pays",)
    history = HistoricalRecords()
   
    def __str__(self):
        """return the name of forme Juridique"""
        return self.currency_code

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Nom du Groupe", unique=True)
    history = HistoricalRecords()

    def __str__(self):
        """return the name of forme Juridique"""
        return self.name

class Company(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100, verbose_name="Raison Sociale", null=False, unique=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Groupe")
    adresse = models.TextField(max_length=300, verbose_name="Adresse", null=True)
    code_postal = models.CharField(max_length=50, verbose_name="Code Postal", null=True)
    city = models.CharField(max_length=100, verbose_name="Ville", null=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name="Pays", null=True, default='212')
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True, verbose_name="Nationalité", blank=True, default='212')
    national_law = models.BooleanField(default=True, verbose_name="De Droit National ?")
    ice = models.CharField(max_length=15, verbose_name="ICE", null=True, blank=True)
    identifiant_fiscal = models.CharField(max_length=10, verbose_name="Identifiant Fiscal", null=True, blank=True)
    cnss = models.CharField(max_length=10, verbose_name="Affiliation CNSS", null=True, blank=True)
    rc = models.CharField(max_length=10, verbose_name="Registre de Commerce", null=True, blank=True)
    tp = models.CharField(max_length=10, verbose_name="Taxe Professionnelle", null=True, blank=True)
    CHOICES_ClasseTP = (
        (30, 'Classe_1 (30%)'),
        (20, 'Classe_2 (20%)'),
        (10, 'Classe_3 (10%)'),
    )
    class_tp = models.IntegerField(verbose_name="Classe TP", choices=CHOICES_ClasseTP, default=20)
    activity = models.TextField(max_length=300, verbose_name="Activité", null=True)

    CHOICES_fiscal_year = (
        (1, 'Janvier'),
        (2, 'Février'),
        (3, 'Mars'),
        (4, 'Avril'),
        (5, 'Mai'),
        (6, 'Juin'),
        (7, 'Juillet'),
        (8, 'Août'),
        (9, 'Septembre'),
        (10, 'Octobre'),
        (11, 'Novembre'),
        (12, 'Décembre'),
    )


    fiscal_year = models.IntegerField(verbose_name="Mois d'Ouverture Année Fiscale", choices=CHOICES_fiscal_year, null=False, default=1)
    create_date = models.DateField(verbose_name="Date de Création", null=True, blank=True)
    
    CHOICES_Statut = (
        (0, 'En Activité'),
        (1, 'En Attente'),
        (2, 'Cessation'),
        (3, 'Liquidation'),
    )
    legal_form = models.ForeignKey(LegalForm, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Forme Juridique")
    share_capital = models.FloatField(verbose_name="Capital Social", blank=True)
    nominal_value = models.FloatField(verbose_name="Valeur Nominale", blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, verbose_name="Devise", default='MAD')
    statut = models.IntegerField(verbose_name="Statut", choices=CHOICES_Statut, default=0)
    terminate_date = models.DateField(verbose_name="Date de Cessation/Dissolution", null=True, blank=True)
    liquidation_date = models.DateField(verbose_name="Date de Liquidation", null=True, blank=True)
    logo = models.ImageField(verbose_name="Joindre Logo", upload_to='files/office/company/logo', null=True, blank=True) # new
    file_rc = models.FileField(verbose_name="Joindre Extrat RC", upload_to='files/office/company/rc', null=True, blank=True) # new
    file_if = models.FileField(verbose_name="Joindre Bulletin IF", upload_to='files/office/company/if', null=True, blank=True) # new
    history = HistoricalRecords()
    

    def __str__(self):
        """return the name of company"""
        return self.name