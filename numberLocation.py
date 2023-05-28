import phonenumbers
import opencage
from myNumber import number

import folium
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "fr")
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "fr"))

key = 'cc47a9fdffb34b509297d1e638beb0bd'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to((myMap))

myMap.save("myLocation.html")