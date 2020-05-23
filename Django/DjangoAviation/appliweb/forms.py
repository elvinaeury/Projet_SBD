from django import forms

MONTH_CHOICES = [(f"0{i}",f"0{i}") for i in range(1,10)] + [("11","11"),("12","12")]

DAY_CHOICES = [(f"0{i}",f"0{i}") for i in range(1,10)] + [(f"{i}",f"{i}") for i in range(10,32)]


#formulaire de recherche par année
class SearchForm(forms.Form):
    year = forms.IntegerField(label="Année",max_value=2020,min_value=1900,help_text="Saisissez une année entre 1900 et 2020")
    
#formulaire de recherche par date jjmmaaaa
class SearchFormPerDate(forms.Form):
    year = forms.IntegerField(label="Année",max_value=2020,min_value=1900,help_text="Saisissez une année entre 1900 et 2020")
    month = forms.ChoiceField(label="Mois",choices=MONTH_CHOICES, help_text="Sélectionnez un mois")
    #month= forms.CharField(widget=forms.Select(choices=MONTH_CHOICES), help_text="Sélectionnez un mois")
    day = forms.ChoiceField(label="Jour",choices=DAY_CHOICES,help_text="Sélectionnez un jour")

#formulaire de recherche entre deux dates 
class SearchFormBetweenTwoDates(forms.Form):
    year_1 = forms.IntegerField(label="Année pour la date de début",max_value=2020,min_value=1900,help_text="Saisissez une année entre 1900 et 2020")
    month_1 = forms.TypedChoiceField(label="Mois pour la date de début",choices=MONTH_CHOICES,required=False,empty_value="01",help_text="Sélectionnez un mois")
    day_1 = forms.TypedChoiceField(label="Jour pour la date de début",choices=DAY_CHOICES,required=False,empty_value="01",help_text="Sélectionnez un jour")

    year_2 = forms.IntegerField(label="Année pour la date de fin",max_value=2020,min_value=1900,help_text="Saisissez une année entre 1900 et 2020")
    month_2 = forms.TypedChoiceField(label="Mois Année pour la date de fin",choices=MONTH_CHOICES,required=False,empty_value="12",help_text="Sélectionnez un mois")
    day_2 = forms.TypedChoiceField(label="Jour Année pour la date de fin",choices=DAY_CHOICES,required=False,empty_value="31",help_text="Sélectionnez un jour")