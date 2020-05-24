from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from appliweb.models import airports, accidents_events, aircrafts, fatalities_report, flight_info, departure_airport, destination_airport

from django.http import HttpResponseRedirect
from .forms import SearchForm, SearchFormPerDate, SearchFormBetweenTwoDates

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage #gestion de la pagination


# Page d'acceuil : vue template2 déclenchant le template analytics2.html 
# Carte du monde : vue worldmap déclenchant le template worldmap.html
#############################################################################################

from .views2 import worldmap, template2

#############################################################################################


#vue pour la table airports
def aeroport(request) :
    airports_list = airports.objects.all()
    nb = airports.objects.count()
    rien = airports.objects.count()==0

    #découpage en pages
    paginator = Paginator(airports_list,50)

    #récupération de la page courante
    page = request.GET.get('page')

    #renvoyer uniquement cette page et pas les autres
    try :
        returnedPage = paginator.page(page)
    except PageNotAnInteger :
        #Si page n'est pas un entier, on rend la première page
        returnedPage = paginator.page(1)
    except EmptyPage :
        #Si page est en dehors des limites, on rend la dernière page
        returnedPage = paginator.page(paginator.num_pages)

    templateVariables = {                                          
            'airports': returnedPage,
            'nb': nb,
            'rien': rien,
            'paginate' : True
        }

    return render(request, 'airports.tmpl', templateVariables)


#vue pour la table accidents_events
def accident(request) :
    accidents_list = accidents_events.objects.all()
    nb = accidents_events.objects.count()
    rien = accidents_events.objects.count()==0

    #découpage en pages
    paginator = Paginator(accidents_list,50)

    #récupération de la page courante
    page = request.GET.get('page')

    #renvoyer uniquement cette page et pas les autres
    try :
        returnedPage = paginator.page(page)
    except PageNotAnInteger :
        #Si page n'est pas un entier, on rend la première page
        returnedPage = paginator.page(1)
    except EmptyPage :
        #Si page est en dehors des limites, on rend la dernière page
        returnedPage = paginator.page(paginator.num_pages)

    templateVariables = {                                          
            'accidents': returnedPage,
            'nb': nb,
            'rien': rien,
            'paginate' : True
        }

    return render(request, 'accidents.tmpl', templateVariables)


############# Recherches dans la table accidents ############

#### Recherche par année #########

#vue associée au formulaire de recherche pour récupérer les paramètres de recherche par année
def get_search_parameters(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            year=form.cleaned_data['year']

            # redirection vers la vue utilisant les paramètres :
            return HttpResponseRedirect(f"/appliweb/accident/{year}/")

    else:
        form = SearchForm()

    return render(request, 'search.tmpl', {'form': form})

#vue pour la table accidents_events avec paramètres de recherche
def accidentSearch(request,year) :
    queryset = accidents_events.objects.filter(identifiant__startswith=year).order_by('identifiant')
    #queryset = accidents_events.objects.filter(identifiant[:4]=year).order_by('identifiant')
    nb = queryset.count()
    rien= queryset.count()==0
    
    #découpage en pages
    paginator = Paginator(queryset,50)

    #récupération de la page courante
    page = request.GET.get('page')

    #renvoyer uniquement cette page et pas les autres
    try :
        returnedPage = paginator.page(page)
    except PageNotAnInteger :
        #Si page n'est pas un entier, on rend la première page
        returnedPage = paginator.page(1)
    except EmptyPage :
        #Si page est en dehors des limites, on rend la dernière page
        returnedPage = paginator.page(paginator.num_pages)

    templateVariables = {                                          
            'accidents': returnedPage,
            'nb': nb,
            'rien': rien,
            'paginate' : True
        }

    return render(request, 'accidents.tmpl', templateVariables)


#### Recherche pour une date précise #########

#vue associée au formulaire de recherche pour récupérer les paramètres de recherche pour une date précise
def get_search_parameters_per_date(request):
    if request.method == 'POST':
        form = SearchFormPerDate(request.POST)
        if form.is_valid():
            year=form.cleaned_data['year']
            month=form.cleaned_data['month']
            day=form.cleaned_data['day']

            # redirection vers la vue utilisant les paramètres :
            return HttpResponseRedirect(f"/appliweb/accident/date/{year}{month}{day}/")

    else:
        form = SearchFormPerDate()

    return render(request, 'search.tmpl', {'form': form})

#vue pour la table accidents_events avec paramètres de recherche par date
def accidentSearchPerDate(request,date) :
    queryset = accidents_events.objects.filter(identifiant__startswith=date).order_by('identifiant')
    #queryset = accidents_events.objects.filter(identifiant[:4]=year).order_by('identifiant')
    nb = queryset.count()
    rien= queryset.count()==0
    
    #découpage en pages
    paginator = Paginator(queryset,50)

    #récupération de la page courante
    page = request.GET.get('page')

    #renvoyer uniquement cette page et pas les autres
    try :
        returnedPage = paginator.page(page)
    except PageNotAnInteger :
        #Si page n'est pas un entier, on rend la première page
        returnedPage = paginator.page(1)
    except EmptyPage :
        #Si page est en dehors des limites, on rend la dernière page
        returnedPage = paginator.page(paginator.num_pages)

    templateVariables = {                                          
            'accidents': returnedPage,
            'nb': nb,
            'rien': rien,
            'paginate' : True
        }

    return render(request, 'accidents.tmpl', templateVariables)


#### Recherche entre deux dates #########

#vue associée au formulaire de recherche pour récupérer les paramètres de recherche pour une date précise
def get_search_parameters_per_dates(request):
    if request.method == 'POST':
        form = SearchFormBetweenTwoDates(request.POST)
        if form.is_valid():
            year_1=form.cleaned_data['year_1']
            month_1=form.cleaned_data['month_1']
            day_1=form.cleaned_data['day_1']

            year_2=form.cleaned_data['year_2']
            month_2=form.cleaned_data['month_2']
            day_2=form.cleaned_data['day_2']

            # redirection vers la vue utilisant les paramètres :
            return HttpResponseRedirect(f"/appliweb/accident/{year_1}{month_1}{day_1}/{year_2}{month_2}{day_2}/")

    else:
        form = SearchFormBetweenTwoDates()

    return render(request, 'search.tmpl', {'form': form})

#vue pour la table accidents_events avec paramètres de recherche par date
def accidentSearchPerDates(request,dateDebut,dateFin) :
    queryset = accidents_events.objects.filter(identifiant__gte=dateDebut,identifiant__lte=dateFin).order_by('identifiant')
    #queryset = accidents_events.objects.filter(identifiant[:4]=year).order_by('identifiant')
    nb = queryset.count()
    rien= queryset.count()==0
    
    #découpage en pages
    paginator = Paginator(queryset,50)

    #récupération de la page courante
    page = request.GET.get('page')

    #renvoyer uniquement cette page et pas les autres
    try :
        returnedPage = paginator.page(page)
    except PageNotAnInteger :
        #Si page n'est pas un entier, on rend la première page
        returnedPage = paginator.page(1)
    except EmptyPage :
        #Si page est en dehors des limites, on rend la dernière page
        returnedPage = paginator.page(paginator.num_pages)

    templateVariables = {                                          
            'accidents': returnedPage,
            'nb': nb,
            'rien': rien,
            'paginate' : True
        }

    return render(request, 'accidents.tmpl', templateVariables)


### vue pour lien de rédirection vers les filtres pour accidents

def tableAccidents(request) :
    return render(request, 'tableAccidents.tmpl')