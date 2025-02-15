# create a mapping of state to abbreviation
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for state, city in list(cities.items()):
    print(f"{state} has the city {city}")
    
# both at the same time
print('*' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has cities {cities[abbrev]}")

print("%" * 10)
state = states.get('Texas')

if not state:
    print("Soory no state is there which you entered")
else:
    print(state)
    
# get a city with a default value
city = cities.get('FD', "Does not exist")
print(city)
