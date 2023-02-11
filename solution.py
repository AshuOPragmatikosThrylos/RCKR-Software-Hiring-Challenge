# Problem statement --> https://rckr.com/careers

# Find latitude and longitude of utmost 20 countries, ordered by population, with a population greater or equal to the population limit given below and have atleast one currency exclusively for themselves. (countries like Madagascar, Sri Lanka but not India, USA). Use the country details from this dataset.
# Your task is to find the sum of the length of all lines (in kms) that can be drawn between co-ordinates of these countries.
# Assume radius of earth: 6371 km
# Round length of each line and final result to 2 decimal points
# If co-ordinates are missing for any country use 0.000 N 0.000 E

# Population limit: 277500
# Note: Population limit will change at random intervals. So please make sure answer is computed for the correct population limit before submitting.

# https://rckr.com/careers?success=1

from math import radians, cos, sin, asin, sqrt
import requests
r = requests.get('https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json')


pop_limit = 100440 # correct ans --> 1902048.98 
top_20 = []

hm = dict()

for i in range(len(r.json())):
	dicts = r.json()[i]['currencies']
	for j in range(len(dicts)):
		key = dicts[j]['code']
		if key in hm.keys():
			value = hm[key]
			hm[key] = value+1
		else:
			hm[key] = 1
		    
def has1UniqueCurr (dicts, hm):
	for i in range(len(dicts)):
		if hm[dicts[i]['code']] == 1 :
			return True
	return False

for i in range(len(r.json())):
    if (r.json()[i]['population'] >= pop_limit and has1UniqueCurr(r.json()[i]['currencies'], hm)):
        top_20.append(r.json()[i])

	
########################################################################################################
#TITLE : Ways to sort list of dictionaries by values in Python – Using lambda function
#SOURCE : https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/

top_20 = sorted(top_20, key=lambda x: x['population'], reverse=False)[:20]


#########################################################################################################
#TITLE : Program for distance between two points on earth
#SOURCE : https://www.geeksforgeeks.org/program-distance-two-points-earth/

def distance(lat1, lat2, lon1, lon2):
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * asin(sqrt(a))
	r = 6371
	return(c * r)
#########################################################################################################


distance_sum = 0.0
while top_20:
    country = top_20.pop(0)
    for i in top_20:
        distance_sum = round(distance_sum + distance(country['latlng'][0], (i['latlng'][0]), country['latlng'][1], i['latlng'][1]), 2)

#Solution
print (round(distance_sum, 2))

