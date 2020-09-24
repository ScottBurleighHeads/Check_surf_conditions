from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Profile")
location = geolocator.geocode("123 Broadbeach gold coast")
print(location.address)
#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
print((location.latitude, location.longitude))
#(40.7410861, -73.9896297241625)

