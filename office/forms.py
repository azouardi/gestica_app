from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class CompanyForm(forms.ModelForm):
        # Ajoutez une case à cocher pour chaque fichier que l'utilisateur peut supprimer
    delete_logo = forms.BooleanField(required=False, label=_('Supprimer le logo'))
    delete_file_rc = forms.BooleanField(required=False, label=_('Supprimer le fichier RC'))
    delete_file_if = forms.BooleanField(required=False, label=_('Supprimer le bulletin IF'))
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Nom de la compagnie'}),
            'group': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'legal_form': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'share_capital': forms.NumberInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Capital Social'}),
            'nominal_value': forms.NumberInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Valeur Nominale'}),
            'national_law': forms.CheckboxInput(attrs={'class': 'form-control form-control-border'}), 
            'ice': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'ICE'}),
            'identifiant_fiscal': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Identifiant Fiscal'}),
            'cnss': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Affiliation CNSS'}),
            'rc': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Registre de Commerce'}),
            'tp': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Taxe Professionnelle'}),

            'class_tp': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'activity': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Activité'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control form-control-border', 'placeholder': 'Adresse'}),
            'code_postal': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Code Postal'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Ville'}),
            'country': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'nationality': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'fiscal_year': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'statut': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'currency': forms.Select(attrs={'class': 'custom-select form-control-border'}),
            'logo': forms.FileInput(attrs={'class': 'form-control form-control-border', 'id': 'customFile', 'accept': 'image/*', 'multiple': False, 'placeholder': 'Joindre Logo'}),
            'file_rc': forms.FileInput(attrs={'class': 'form-control form-control-border', 'id': 'customFile'}),
            'file_if': forms.FileInput(attrs={'class': 'form-control form-control-border', 'id': 'customFile'}),
            'create_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control form-control-border', 'type': 'date'}),
            'terminate_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control form-control-border', 'type': 'date'}),
            'liquidation_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control form-control-border', 'type': 'date'}),
        }
                
            





    # class Month(models.IntegerChoices):
    #     Decembre = 1, ('Décembre')
    #     Janvier = 2, ('Janvier')
    #     Fevrier = 3, ('Février')
    #     Mars = 4, ('Mars')
    #     Avril = 5, ('Avril')
    #     Mai = 6, ('Mai')
    #     Juin = 7, ('Juin')
    #     Juillet = 8, ('Juillet')
    #     Aout = 9, ('Août')
    #     Septembre = 10, ('Septembre')
    #     Octobre = 11, ('Octobre')
    #     Novembre = 12, ('Novembre')

    # fiscal_year = models.IntegerField(verbose_name="Mois d'Ouverture Année Fiscale", choices=Month.choices, null=False, default=1)
    # create_date = models.DateField(verbose_name="Date de Création", null=True, blank=True)
    
    # class Statut(models.IntegerChoices):
    #     En_Attente = 0, ('En Attente')
    #     Actif = 1, ('Actif')
    #     Suspendu = 2, ('Suspendu')
    #     InActif = 3, ('InActif')

    # nominal_value = models.FloatField(verbose_name="Valeur Nominale", blank=True)
    # currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, verbose_name="Devise", default='MAD')
    # statut = models.IntegerField(verbose_name="Statut", choices=Statut.choices, default=0)
    # terminate_date = models.DateField(verbose_name="Date de Cessation/Dissolution", null=True, blank=True)
    # liquidation_date = models.DateField(verbose_name="Date de Liquidation", null=True, blank=True)
    # logo = models.ImageField(verbose_name="Joindre Logo", upload_to='files/office/company/logo', null=True, blank=True) # new
    # file_rc = models.FileField(verbose_name="Joindre Extrat RC", upload_to='files/office/company/rc', null=True, blank=True) # new
    # file_if = models.FileField(verbose_name="Joindre Bulletin IF", upload_to='files/office/company/if', null=True, blank=True) # new
    # history = HistoricalRecords()
    