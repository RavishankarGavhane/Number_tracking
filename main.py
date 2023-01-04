from geopy.geocoders import Nominatim

loc =  Nominatim(user_agent="GetLoc")

getLoc = loc.geocode("Pune Maharashtra")
print(getLoc.address)
print("Latitude = ", getLoc.latitude, "\n")
print("longitude = ", getLoc.longitude)

from  geopy.geocoders import Nominatim

geoLoc = Nominatim(user_agent= "GetLoc")
locname = geoLoc.reverse("18.521428, 73.8544541")
print(locname.address)
