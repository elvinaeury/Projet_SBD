from django.db import models

# Create your models here.

class airports(models.Model) :
    code_iata = models.CharField(max_length=3,null=True)
    code_icao = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    altitude = models.FloatField(null=True)

class accidents_events(models.Model) :
    identifiant = models.CharField(max_length=11,unique=True)
    week_day = models.CharField(max_length=10,null=True)
    #date = models.DateTimeField()
    date = models.CharField(max_length=11)
    time = models.CharField(max_length=5,null=True)
    type_event = models.CharField(max_length=2)
    phase = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    total_occupants = models.IntegerField(null=True)
    total_fatalities = models.IntegerField(null=True)
    aircraft_damage = models.CharField(max_length=100,null=True)
    aircraft_fate = models.CharField(max_length=100,null=True)

class aircrafts(models.Model) :
    id_aircraft = models.ForeignKey(accidents_events, on_delete=models.CASCADE)
    type_aircraft = models.CharField(max_length=100,null=True)
    number_engines = models.IntegerField(null=True)
    type_engines = models.CharField(max_length=100,null=True)
    first_flight = models.IntegerField(null=True)
    cycles = models.IntegerField(null=True)
    total_airframe_hours = models.IntegerField(null=True)
    registration = models.CharField(max_length=100,null=True)
    c_n_msn = models.CharField(max_length=100,null=True)

class fatalities_report(models.Model) :
    id_report = models.ForeignKey(accidents_events, on_delete=models.CASCADE)
    crew_fatalities = models.IntegerField(null=True)
    passengers_fatalities = models.IntegerField(null=True)
    collision_casualties = models.IntegerField(null=True)
    ground_casualties = models.IntegerField(null=True)
    status = models.CharField(max_length=100,null=True)

class flight_info(models.Model) :
    id_flight = models.ForeignKey(accidents_events, on_delete=models.CASCADE)
    operator = models.CharField(max_length=100,null=True)
    nature = models.CharField(max_length=100,null=True)
    flight_number = models.CharField(max_length=20,null=True)
    #departure_airport = models.ForeignKey(airports,on_delete=models.PROTECT,to_field=airports.code_icao)
    #destination_airport = models.ForeignKey(airports,on_delete=models.PROTECT)
    crew_number = models.IntegerField(null=True)
    passengers_number = models.IntegerField(null=True)

class departure_airport(models.Model) :
    flight = models.ForeignKey(flight_info,on_delete=models.CASCADE)
    icao = models.ForeignKey(airports,on_delete=models.PROTECT)

class destination_airport(models.Model) :
    flight = models.ForeignKey(flight_info,on_delete=models.CASCADE)
    icao = models.ForeignKey(airports,on_delete=models.PROTECT)
