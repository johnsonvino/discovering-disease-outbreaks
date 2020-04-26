import geonamescache

gc = geonamescache.GeonamesCache()
#cities = gc.get_cities()
#print(cities.values())
#print([v for k,v in cities.items() if k == 'name'])

cities = ([[v for k,v in values.items() if k == 'name'] for key,values in gc.get_cities().items()])

print(type(cities))
print(cities[:10])