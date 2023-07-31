import phonenumbers
##import folium

from myNumber import number

from phonenumbers import geocoder

##from opencagedata.com
key = "f95bbeb9361d49ff9217ac292ecc6480"

sanNumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(sanNumber, "en")

print(yourlocation)

##getting the service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)

print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourlocation)

results = geocoder.geocode(query)

##print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)
