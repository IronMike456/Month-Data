"""Required and optional arguments
In Python, several built-in functions require arguments. Some built-in functions make arguments optional. Built-in functions are immediately available, so you don't need to import them explicitly.

An example of a built-in function that requires an argument is any(). This function takes an iterable (for example, a list) and returns True if any item in the iterable is True. Otherwise, it returns False."""

any([True, False, False])

# Check if any of the items in a list are True

"""Required  arguments """

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
distance_from_earth("Moon") # 238,885
distance_from_earth("Saturn") # Unable to compute to that destination


""" Multiple arguments """
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

total_days = days_to_complete(238855, 75)
round(total_days)

## Although passing functions directly into other functions as input is useful, there is potential for reduced readability. This pattern is especially problematic when the functions require many arguments.


"""Use key words arguments
Optional arguments require a default value assigned to them. These named arguments are called keyword arguments. 
Keyword argument values must be defined in the functions themselves.
When you're calling a function that's defined with keyword arguments, it isn't necessary to use them at all.
"""
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    timedelta(days=12)
    return arrival.strftime("Arrival: %A %H:%M")

arrival_time()

""" Mixing arguments and key words"""

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

arrival_time("Moon")

"""Variable arguments 
Arguments in functions are required. But when you're using variable arguments, the function allows any number of arguments (including 0) to be passed in. 
The syntax for using variable arguments is prefixing a single asterisk (*) before the argument's name.
"""

def variable_length(*args):
    print(args)

variable_length("one", "two")

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
"""Keywords arguments
For a function to accept any number of keyword arguments, you use a similar syntax. In this case, a double asterisk is required
"""

def variable_length(**kwargs):
    print(kwargs)


variable_length(tanks=1, day="Wednesday", pilots=3)

# If you're already familiar with Python dictionaries, you'll notice that variable-length keyword arguments are assigned as a dictionary. To interact with the variables and values, use the same operations as a dictionary.

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
