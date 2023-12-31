import requests
import urllib

api_url = "https://www.mapquestapi.com/directions/v2/route?"
key = "iSbemi1OPlV3aOG59FxzsiHJd67rSOA9"
origin ="Tijuana,Bugambilia 99"
destination ="Tijuana, Instituto Tecnologico de Tijuana Tomas Aquino"
      
url = api_url + urllib.parse.urlencode({"key":key, "from":origin, "to":destination})
json_data = requests.get(url).json()
status_code = json_data["info"]["statuscode"]
if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"] * 1.61

        print("=================================================================================")
        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
        print(f"Duración del viaje: {trip_duration}.")
        print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
        print("=================================================================================")
        print("Indicaciones del viaje")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            distance_remaining = distance - each["distance"] * 1.61            
            print(each["narrative"] + " (" + str("{:.2f}".format(distance_remaining)) + " Km faltantes)")
            distance = distance_remaining