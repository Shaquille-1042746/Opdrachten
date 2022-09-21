#Integers
#Display large numbers in a readable format
import imp
from re import X
from time import time
from turtle import distance

people = 7861304740
print(people)
people = 7_861_304_740
print(people)

#Calculations with big numbers
meals = 3
people_eat= people * meals
print(people_eat)

days = 365
meals_per_year = people_eat * days
print(meals_per_year)
type(meals_per_year)

#Float
#Ethernet capacity
ethernet_speed_mbs = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbs * efficiency
print(maximum_capacity)

#Print capacity used on the ethernet
download_speed_average = 96.25
usage = ethernet_speed_mbs / download_speed_average
print(usage)

#Speed of light in m/s
speed_of_light = 299_792_458

#Distance Rotterdam / New York in km
distance_Rotterdam_NewYork = 5_862.03

#Distance Rotterdam to New York in meters divided by the speed of the light
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(f'Time to reach New York is: {time_to_reach_NYC} seconds => {time_to_reach_NYC * 1000.0} milliseconds.')

#Whats is the data type?
type(time_to_reach_NYC)

#String
ship = 'Titanic'
print(ship)
ship ="Titanic"
print(ship)
ship = """Titanic"""
print(ship)

#Note: The sentence could contain an apostrophe
#Using an apostrophe is possible if you use the double quotes to surround the string
sentence = "He doesn't think it's a good idea to spend all his money on video games."
print(sentence)

#Gebruik """ """ als je meerdere regels tekst moet tonen
paragraph = """Computer Technology means all designs, drawings, procedures
(including design, manufacturing, test and maintenance procedures),
specifications, software (other than as described within the meaning of the term
"Software" defined elsewhere herein), printed circuit board art work, integrated
circuit masks, test equipment, tools, fixtures, documentation, training materials,
and information, in whatever form, related to, useful, utilizable or necessary in
the design, manufacture, test and/or maintenance of the computer system, or relate
to any Technology Licenses."""
print(paragraph)

#With the len() function you can ask how many characters the string has
characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")

year = 1936
inventor = "Alan Turing"
name_of_machine = "Automatic Machine"
#Note: Within the text double quotes are used. We need to use single quotes to embrace the string
invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_machine}).'
print(invention)

#What is the data type?
type(invention)

#Boolean
logged_in = False
print(logged_in)

netwerk_activity = True
print(netwerk_activity)

user_name = "John Doe"
entered_name = input("User name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name
print(f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")
print(f"The enter name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")

lights_on = False
lock_closed = True
#Not keert de waarde van een boolean om not True is hetzelfde als False
#Andersom is not False dus True
alarm_activated = not lights_on and lock_closed
print(f"The alarm is activated, is: {alarm_activated}")

#Berekening
import math

x = 9.1
term1 = (3 * x) - 1
term2 = 1 + x
term3 = (term2) **2
y = math.sqrt(term1) + term3
print(f'De waarde van y = {y} als x = {x}')

#Berekening
import math

a = 0.87
b = 22.7
c = 5.03
term1 = b**2
term2 = 4 * a * c
term3 = term1 - term2
term4 = math.sqrt(term3)
term5 = -b + term4
term6 = 2 * a 
y = term5 / term6
print(f'De waarde van y = {y} als a = {a}, b = {b} en c = {c}')

#Containers
#Terminal information
containers_unloaded = 331
unload_time = 441
containers_loaded = 287
load_time = 295

#Calculate the averages containers per minute
average_unload_time = unload_time / containers_unloaded
average_load_time = load_time / containers_loaded
print(f'De gemiddelde lostijd bedraag {average_unload_time} minuten per container')
print(f'De gemiddelde lostjd bedraagt {average_load_time}')

#Berekening
#Information
t = 4
v = 179875474.8
c = 299_792_458

# Breakup the formula
term1 = v**2
term2 = c**2
term3 = term1 / term2
term4 = 1 - term3
term5 = v * term4
term6 = 1 / term5
delta = t * term6
#Display result
print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0} minuten op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0 * 60.0} seconden op de tuinstoel.')
