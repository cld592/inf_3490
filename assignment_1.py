import csv

# Read data file
distance_table = []
with open('D:\INF3490\european_cities.csv') as file:
  reader = csv.reader(file,delimiter=';')
  # First row is the city names
  city_names = reader.next()
  # The rest of the rows are the distance table
  for row in reader:
    distance_table.append([float(cell) for cell in row])

# List the city names
print city_names
# Print out the size of the table, should be square
print len(distance_table), len(distance_table[0])
# Look up a distance and print it
city_A = 3 # Simply refer to cities by
city_B = 5 # their index in the table
#print 'The distance from',city_names[city_A],'to',city_names[city_B],'is',distance_table[city_A][city_B],'km'


def distance(cities):
  total=0
  g=0
  for i in range(0,len(cities)-1):
    total=total+distance_table[cities[i]][cities[i+1]]
  return total

import itertools



alpha=[0,1,2,3,4,5,6,7,8,9]

print distance(alpha)

lista=[]

def best_distance(city):
    best=0
    new_distance=0
    ritorno=0
    best=distance(city)
    for f in itertools.permutations(city,10):
        ritorno=distance_table[f[0]][f[len(f)-1]]
        new_distance=distance(f)+ritorno
        if new_distance<best:
            best=new_distance
    return best

print best_distance(alpha)
