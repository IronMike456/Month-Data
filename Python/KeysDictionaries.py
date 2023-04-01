""" Create a dictionary """
planet = {
    'name': 'Earth',
    'moons': 1
}

""" Read data from a dictionary """
print(planet.get('name'))

planet.get('moons') 
print(planet['name'])

"""Modify dictionary values"""
# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

""" Add data into a dictionary """

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
### Every key in python is case sensitive 
""" Remove  a key """
planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

""" Data complex """

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }


""" The keys() method returns a list object that contains all the keys. You can use this method to iterate through all items in the dictionary. 
Imagine you have the following dictionary, storing the last three months of rainfall. """ 

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1,
    "january": 3.4 
}

# Let's say you want to display the list of all rainfall. You can type out the name of each month, but that would be tedious.

for key in rainfall.keys(): #Gets the value word of the dictionary, in this case are the month such as 'october' 
    print(f'{key}: {rainfall[key]}cm') # Prints the key (word) and the related data. 


"""Determine if a key exists in a dictionary
When you update a value in a dictionary, Python will either overwrite the existing value or create a new one, 
if the key doesn't exist. If you wish to add to a value rather than overwriting it, you can check to see if the key exists by using in. For example, 
if you want to add a value to December or create a new one if it doesn't exist, you can use the following:"""

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

print(f'{rainfall["december"]}')

# Because december exists, the value will be 3.1

""" Retrieve all values
Similar to keys(), values() returns the list of all values in a dictionary without their respective keys. 
values() can be helpful when you're using the key for labeling purposes, such as the preceding example, in which the keys are the name of the month. 
You can use values() to determine the total rainfall amount:"""

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print("\nRetrieve all values ")

print(f'There was {total_rainfall}cm in the last quarter')

"""Excercise"""

""" In this scenario, you will calculate both the total number of moons in the solar system and the average number of moons a planet has. 
You will do this by using a dictionary object."""

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

""" Obtain a list of moons and number of planets 
Python dictionaries allow you to retrieve all the values and keys by using the values and keys methods, respectively. 
Each method returns a list containing the data, which can then be used like a regular Python list.
"""

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

"""Determine the average number of moons
You will finish this exercise by determining the average number of moons. Start by creating a variable named total_moons; 
this will be your counter for the total number of moons. Then add a for loop to loop through the list of moons, adding each value to total_moons. 
Finally, calculate the average by dividing total_moons by total_planets and displaying the value."""

otal_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')