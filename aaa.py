### NOTE THERE MIGHT BE USAGE LIMITS: ChatGPT says I shouldn't make more than 1 request per second with geolocator.geocode
### OTHERWISE MIGHT HAVE IP ADDRESS BLOCKED FOR EXCEEDING USAGE LIMITS.
    ### POSSIBLE SOLUTIONS: i) Use a batch geocoding service (e.g. Google Geocoding API or BatchGeo)
    ###                    ii) Use a commercial geocoding service

# For finding coordinates of locations (needed for G)
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.latitude, location.longitude)

# To compute edge weights in G from the above step
from geopy.distance import geodesic
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print('geopy distance: ', geodesic(newport_ri, cleveland_oh).miles)
print('geopy distance: ', geodesic(cleveland_oh, newport_ri).miles)

L=[2,3,5,6]
print(L[:-1])
