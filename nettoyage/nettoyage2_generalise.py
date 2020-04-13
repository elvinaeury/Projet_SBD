import pandas as pd
import re
import warnings

warnings.filterwarnings("ignore")

final_names =["identifiant",
              "week_day",
              "date",
              "time",
              "type_event",
              "phase",
              "location",
              "country",
              "total_occupants",
              "total_fatalities",
              "aircraft_damage",
              "aircraft_fate",
              "type_aircraft",
              "number_engines",
              "type_engines",
              "first_flight",
              "cycles",
              "total_airframe_hours",
              "registration",
              "c_n_msn",
              "operator",
              "nature",
              "flight_number",
              "departure_airport_name",
              "departure_airport_IATA",
              "departure_airport_ICAO",
              "departure_airport_country",
              "destination_airport_name",
              "destination_airport_IATA",
              "destination_airport_ICAO",
              "destination_airport_country",
              "crew_number",
              "passengers_number",
              "crew_fatalities",
              "passengers_fatalities",
              "collision_casualties",
              "ground_casualties",
              "status"]

names=["identifiant",
       "status",
       "date",
       "time",
       "type_aircraft",
       "operator",
       "operating_for",
       "on_behalf_of",
       "leased_from",
       "registration",
       "c_n_msn",
       "first_flight",
       "total_airframe_hours",
       "year_built",
       "engines",
       "cycles",
       "crew","passengers",
       "ground_casualties",
       "collision_casualties",
       "aircraft_damage",
       "aircraft_fate",
       "location",
       "phase",
       "nature",
       "departure_airport",
       "destination_airport",
       "flight_number",
       "probable_cause",
       "total"]

annees = [k for k in range(1919,2021)]
annees.append(1900)

annees_problematiques = set()

for annee in annees :

    p=f"bonnes_donnees2/data_{annee}.csv"
    dframe=pd.read_csv(p,sep=",",skiprows=[0],names=names)
    if annee==1900 :
        dframe["date"]="xxxx"

    p_record = f"record2/data_{annee}.csv"
    record_names = ["identifiant","date","type_aircraft","registration","operator","fatalities","location","type_event"]
    cols = [0,1,2,3,4,5,6,9]
    dfrecord=pd.read_csv(p_record,sep=",",usecols=cols,skiprows=[0],names=record_names)
    if annee==1900 :
        dfrecord["date"]="xxxx"

    dframe.drop(["year_built","operating_for","leased_from","on_behalf_of","probable_cause"],axis=1,inplace=True)

    motif=re.compile(r"^\s$")
    for col in dframe.columns :
        for i in dframe.index :
            if str(dframe.loc[i,col])=="nan" or bool(motif.match(str(dframe.loc[i,col]))) or str(dframe.loc[i,col])=="?" or str(dframe.loc[i,col])=='':
                dframe.loc[i,col]="-"

    for col in dfrecord.columns :
        for i in dfrecord.index :
            if str(dfrecord.loc[i,col])=="nan" or bool(motif.match(str(dfrecord.loc[i,col]))) or str(dfrecord.loc[i,col])=="?" or str(dfrecord.loc[i,col])=='':
                dfrecord.loc[i,col]="-"

    n=dframe.shape[0]
    colonne=["-" for i in range(n)]
    dframe.insert(1,"week_day",colonne)
    dic={"January":"JAN","February":"FEB","March":"MAR","April":"APR","May":"MAY","June":"JUN","July":"JUL","August":"AUG","September":"SEP","October":"OCT","November":"NOV","December":"DEC"}
    #dic.keys()

    liste=[f"{j}" for j in range(1,10)]
    for i in dframe.index :
        date = dframe.loc[i,"date"].split(sep=" ")
        if len(date)==4 :
            dframe.loc[i,"week_day"]=date[0]
            if date[1] in liste : date[1]="0"+date[1]
            dframe.loc[i,"date"] = date[1]+"-"+dic[date[2]]+"-"+date[3]
        if len(date)==3 :
            if date[0] in liste : date[0]="0"+date[0]
            if date[1] in dic.keys():
                dframe.loc[i,"date"] = date[0]+"-"+dic[date[1]]+"-"+date[2]
            else :
                dframe.loc[i,"date"] = date[0]+"-"+date[1]+"-"+date[2]
        if len(date) ==2 :
            if date[0] in dic.keys() :
                dframe.loc[i,"date"] = "xx"+"-"+dic[date[0]]+"-"+date[1]
            else :
                dframe.loc[i,"date"] = "xx"+"-"+date[0]+"-"+date[1]
        if len(date) == 1:
            dframe.loc[i,"date"] = "xx"+"-"+"xxx"+"-"+date[0]

    for i in dfrecord.index :
        date = dfrecord.loc[i,"date"].split(sep="-")
        if len(date) >= 2 :
            if date[1] not in dic.values():
                #try :
                dfrecord.loc[i,"date"] = "xx"+"-"+"xxx"+"-"+date[2]
                #except IndexError as ind :
                #print(date, annee, " : ", i)
            elif date[0]=="??" :
                dfrecord.loc[i,"date"] = "xx"+"-"+date[1]+"-"+date[2]
        else :
            dfrecord.loc[i,"date"] = "xx"+"-"+"xxx"+"-"+date[0]

    dframe.insert(4,"type_event",colonne)
    for i in dframe.index :
        identifiant=dframe.loc[i,"identifiant"]
        df=dfrecord[dfrecord.identifiant==identifiant]
        if df.shape[0]==1 :  
            dframe.type_event[i]=df.type_event[df.index[0]]
            operator = df.operator[df.index[0]]
            operator_i = re.compile(r"^[^,]+")
            found=operator_i.search(operator)
            try :
                dframe.operator[i] = found.group()
            except AttributeError as e :
                print(f"échec d'ajout de modification de l'opérateur :    \n   année : {annee}   \n   élément {i} d'identifiant : {identifiant} \n   operator : {operator} \n   Erreur : {e}")
                annees_problematiques.add(annee)
        else :
            print(f"échec pour l'élément {i} de l'année {annee} : \n   {df.shape[0]} correspondances possibles pour l'identifiant {identifiant}")
            annees_problematiques.add(annee)

    dframe["country"]=colonne
    dframe["total_occupants"]=colonne
    dframe["total_fatalities"]=colonne
    dframe["number_engines"]=colonne
    dframe["type_engines"]=colonne
    dframe["crew_number"]=colonne
    dframe["passengers_number"]=colonne
    dframe["crew_fatalities"]=colonne
    dframe["passengers_fatalities"]=colonne
    dframe["departure_airport_name"]=colonne
    dframe["departure_airport_IATA"]=colonne
    dframe["departure_airport_ICAO"]=colonne
    dframe["departure_airport_country"]=colonne
    dframe["destination_airport_name"]=colonne
    dframe["destination_airport_IATA"]=colonne
    dframe["destination_airport_ICAO"]=colonne
    dframe["destination_airport_country"]=colonne

    for i in dframe.index :
        
        time = dframe.time[i]
        motif_i = re.compile(r"\d\d:\d\d")
        found = motif_i.search(time)
        if bool(found) :
            dframe.time[i] = found.group()
        
        engines = dframe.engines[i]
        motif_i = re.compile(r"^\s(\d+)\s(.+)$")
        found = motif_i.search(engines)
        if bool(found) :
            dframe.number_engines[i] = found.group(1)
            dframe.type_engines[i] = found.group(2)
        else :
            dframe.type_engines[i]=engines
        
        crew = dframe.crew[i]
        motif_i = re.compile(r"(\d*)\s/\s\D+(\d*)")
        found = motif_i.search(crew)
        try :
            dframe.crew_fatalities[i] = int(found.group(1))
        except ValueError as err :
            dframe.crew_fatalities[i]="-"
        try :
            dframe.crew_number[i] = int(found.group(2))
        except ValueError as err :
            dframe.crew_number[i]="-"
            
        passengers = dframe.passengers[i]
        motif_i = re.compile(r"(\d*)\s/\s\D+(\d*)")
        found = motif_i.search(passengers)
        try :
            dframe.passengers_fatalities[i] = int(found.group(1))
        except ValueError as err :
            dframe.passengers_fatalities[i]="-"
        try :
            dframe.passengers_number[i] = int(found.group(2))
        except ValueError as err :
            dframe.passengers_number[i]="-"
            
        total = dframe.total[i]
        motif_i = re.compile(r"(\d*)\s/\s\D+(\d*)")
        found = motif_i.search(total)
        try :
            dframe.total_fatalities[i] = int(found.group(1))
        except ValueError as err :
            dframe.total_fatalities[i]="-"
        try :
            dframe.total_occupants[i] = int(found.group(2))
        except ValueError as err :
            dframe.total_occupants[i]="-"
        
        location=dframe.location[i]
        motif_i = re.compile(r"^(.*?)\s+\(\s+(\D.*)\)")
        found = motif_i.search(location)
        dframe.location[i]=found.group(1)
        dframe.country[i]=found.group(2)

        first=dframe.first_flight[i]
        motif_i = re.compile(r"^\s*(\d\d\d\d)")
        #print(first)
        #print(type(first))
        found = motif_i.search(str(first))
        if bool(found) :
            dframe.first_flight[i] = int(found.group())
        
        for nom in ["departure_airport","destination_airport"] :
            airport=dframe.loc[i,nom]
            motif_i = re.compile(r"^([^,]*),?.*?\s+\((...)/(....)\),\s(.*)$")
            found = motif_i.search(airport)
            if bool(found) :
                dframe.loc[i,f"{nom}_name"] = found.group(1)
                dframe.loc[i,f"{nom}_IATA"] = found.group(2)
                dframe.loc[i,f"{nom}_ICAO"] = found.group(3)
                dframe.loc[i,f"{nom}_country"] = found.group(4)
        
        for nom in ["ground_casualties","collision_casualties"] :
            casualties=dframe.loc[i,nom]
            motif_i = re.compile(r"\d+")
            found = motif_i.search(casualties)
            if bool(found) :
                dframe.loc[i,nom] = int(found.group())

    dframe.drop(["engines","crew","passengers","total","departure_airport","destination_airport"],axis=1,inplace=True)

    dframe=dframe.reindex(columns=final_names)

    dframe.to_csv(f"donnees_traitees/data_{annee}.csv",index=False,header=True)

print(f"""
------------------------------------------------------------------------------- \n
{len(annees_problematiques)} années probématique(s) rencontrée(s) au total : {annees_problematiques} \n
--------------------------------------------------------------------------------
""")