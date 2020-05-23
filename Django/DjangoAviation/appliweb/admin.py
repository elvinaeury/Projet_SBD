from django.contrib import admin

# Register your models here.

from .models import airports, accidents_events, aircrafts, fatalities_report, flight_info, departure_airport, destination_airport

admin.site.register(airports)
admin.site.register(accidents_events)
admin.site.register(aircrafts)
admin.site.register(fatalities_report)
admin.site.register(flight_info)
admin.site.register(departure_airport)
admin.site.register(destination_airport)