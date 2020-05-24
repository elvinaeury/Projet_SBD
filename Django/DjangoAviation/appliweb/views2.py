from django.http import HttpResponse
from appliweb.models import airports,accidents_events,aircrafts,departure_airport,destination_airport,fatalities_report,flight_info
from datetime import date
from django.shortcuts import render
from django.template import RequestContext
#from django.shortcuts import render_to_response
import pandas as pd
from django.db.models import Q,FilteredRelation,F,Count
from django.db.models import Max
from django.db.models.functions import ExtractYear





from matplotlib.backends.backend_agg import FigureCanvasAgg
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")



# Create your views here.




def worldmap(request):
    return render(request, 'worldmap.html')



def team(request):
    return render(request, 'team.html')



def template2(request):
    t=date.today()

    
    cas=fatalities_report.objects.only('id').filter(Q(crew_fatalities__gte=0)|Q(passengers_fatalities__gte=0)|Q(collision_casualties__gte=0)|Q(ground_casualties__gte=0))
    fatal=accidents_events.objects.filter(Q(total_fatalities__gte=0)).count()
    destroyed=accidents_events.objects.filter(Q(total_fatalities__gte=0)|Q(aircraft_damage__contains='Destroyed')).count()
    missing=accidents_events.objects.filter(Q(total_fatalities__gte=0)|Q(aircraft_damage__contains='Missing')).count()
    
    earliest_=accidents_events.objects.earliest('id').date
    
    types_engs = aircrafts.objects.aggregate(Max('type_engines'))['type_engines__max']
    types_air=aircrafts.objects.exclude(type_aircraft__contains='unknown').aggregate(Max('type_aircraft'))['type_aircraft__max']
    days=accidents_events.objects.exclude(total_fatalities=0).aggregate(Max('week_day'))['week_day__max']
    
    accidented_aircrafts=aircrafts.objects.only('type_aircraft').filter(id_aircraft__in=cas.values('id')).exclude(type_aircraft__contains='unknown').aggregate(Max('type_aircraft'))['type_aircraft__max']
  
    worst_id=accidents_events.objects.exclude(total_fatalities__isnull=True).latest('total_fatalities').id
    worst_country=accidents_events.objects.exclude(total_fatalities__isnull=True).latest('total_fatalities').country
    worst_date=accidents_events.objects.exclude(total_fatalities__isnull=True).latest('total_fatalities').date
    
    worst_aircraft=aircrafts.objects.filter(id=worst_id).aggregate(Max('type_aircraft'))['type_aircraft__max']
    


    country1=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').values_list('country').annotate(count_country=Count('country')).order_by('-count_country')[0][0]
    country2=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').values_list('country').annotate(count_country=Count('country')).order_by('-count_country')[1][0]
    country3=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').values_list('country').annotate(count_country=Count('country')).order_by('-count_country')[2][0]
    country4=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').values_list('country').annotate(count_country=Count('country')).order_by('-count_country')[3][0]
    country5=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').values_list('country').annotate(count_country=Count('country')).order_by('-count_country')[4][0]

    number1=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').values_list('country').annotate(count_country=Count('country')).aggregate(max_value=Max('count_country'))['max_value']
    number2=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').exclude(country__contains=country1).values_list('country').annotate(count_country=Count('country')).aggregate(max_value=Max('count_country'))['max_value']
    number3=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').exclude(country__contains=country1).exclude(country__contains=country2).values_list('country').annotate(count_country=Count('country')).aggregate(max_value=Max('count_country'))['max_value']
    number4=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').exclude(country__contains=country1).exclude(country__contains=country2).exclude(country__contains=country3).values_list('country').annotate(count_country=Count('country')).aggregate(max_value=Max('count_country'))['max_value']
    number5=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).exclude(country__contains='Unknown').exclude(country__contains=country1).exclude(country__contains=country2).exclude(country__contains=country3).exclude(country__contains=country4).values_list('country').annotate(count_country=Count('country')).aggregate(max_value=Max('count_country'))['max_value']


    total_count=accidents_events.objects.exclude(total_fatalities=0).exclude(total_fatalities__isnull=True).count()
    
    percent1=round(number1/total_count*100,2)
    percent2=round(number2/total_count*100,2)
    percent3=round(number3/total_count*100,2)
    percent4=round(number4/total_count*100,2)
    percent5=round(number5/total_count*100,2)

    
    
    perc_pass=round((flight_info.objects.filter(nature__contains='Passenger').count()/flight_info.objects.only('id').count())*100,2)
    perc_military=round((flight_info.objects.filter(nature__contains='Military').count()/flight_info.objects.only('id').count())*100,2)
    perc_cargo=round((flight_info.objects.filter(Q(nature__contains='Cargo')|Q(nature__contains='Ferry')).count()/flight_info.objects.only('id').count())*100,2)
    perc_test=round((flight_info.objects.filter(Q(nature__contains='Test')|Q(nature__contains='research')).count()/flight_info.objects.only('id').count())*100,2)



    return render(request,'analytics2.html',
                  {
                      'title':t,
                      'percent1': percent1,'percent2': percent2,'percent3': percent3,'percent4': percent4,'percent5': percent5,
                      'country1': country1,'country2': country2,'country3': country3,'country4': country4,'country5': country5,
                      'number1': number1,'number2': number2,'number3': number3,'number4': number4,'number5': number5,
                      'nb1': cas.count(),
                      'fatal':fatal,
                      'destroyed':destroyed,
                      'types_air':types_air,
                      'types_engs':types_engs,
                      'missing':missing,
                      'earliest_':earliest_,
                      'accidented_aircrafts':accidented_aircrafts,
                      'days':days,
                      'worst_id':worst_id,
                      'worst_aircraft': worst_aircraft,
                      'worst_date':worst_date,
                      'worst_country':worst_country,
                      'perc_pass':perc_pass,
                      'perc_military':perc_military,
                      'perc_cargo':perc_cargo,
                      'perc_test':perc_test,
                      
                          })
    


