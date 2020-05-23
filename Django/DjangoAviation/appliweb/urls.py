from django.urls import path, re_path
from . import views

urlpatterns = [

    #####################################################
    # Page d'accueil
    path('worldmap/',views.worldmap,name='world'),
    
    # map
    path('',views.template2,name='template2'), 
    #######################################################

    # Affichage des tables
    path('aeroport/',views.aeroport,name='aeroport'), # table aéroports
    path('accident/',views.accident,name='accident'), # table accidents

    # recherche par année dans la table accident
    path('research/',views.get_search_parameters), # url affichant le formulaire de recherche par année
    re_path(r'^accident/(\d+)/$',views.accidentSearch), # url traitant le résulat du formulaire de recherche par année

    # recherche par date dans la table accident
    path('research/date/',views.get_search_parameters_per_date), # url affichant le formulaire de recherche par date
    re_path(r'^accident/date/(\d+)/$',views.accidentSearchPerDate), # url traitant le résulat du formulaire de recherche par date

    # recherche entre deux dans la table accident
    path('research/dates/',views.get_search_parameters_per_dates), # url affichant le formulaire de recherche entre deux dates
    re_path(r'^accident/(\d+)/(\d+)/$',views.accidentSearchPerDates), # url traitant le résulat du formulaire de recherche entre deux dates

    # lien de gestion de la table accident à mettre sur la page d'accueil
    path('tableaccidents/',views.tableAccidents),
]