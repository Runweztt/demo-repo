animals =[
    {"name": "capybara","group": "mammals", "weight": 110},
    {"name": "hedgehog","group": "mammals", "weight": 568},
    {"name": "ostrich","group": "bird", "weight": 678},
    {"name": "elephant","group": "mammals", "weight": 788},
    {"name": "python","group": "reptile", "weight": 789},
    {"name": "humming bird","group": "bird", "weight": 110},
    {"name": "black cobra","group": "reptile", "weight": 7890},
    {"name": "desert snake","group": "reptile", "weight": 1198},
    {"name": "lion","group": "mammals", "weight": 1760},
    {"name": "color bird","group": "bird", "weight": 170},
    {"name": "monkey","group": "mammals", "weight": 11890}
]
#  print out animal that is heavier than 100
# first we loop through the dictionary 
# write an if statement to get the animal that heavier than 100 
# print the result

for animal in animals:
    if(animal["weight"] > 100):
      print(animal ["name"])


# print out the heaviest animal 
# first we loop through the dicts 
# find out the heaviest 
# compare animal with weight 

heaviest =animals[0]
for animal in animals:
   if(animal["weight"]> heaviest["weight"]):
      heaviest=animal
print(heaviest)


# print out the lightiest animal 
# first we loop through the dicts 
# find out the lightiest
# compare animal with weight 

lightiest =animals[0]
for animal in animals:
   if(animal["weight"]<lightiest["weight"]):
      lightiest=animal
print(lightiest)


# print out the mammals as a  list

mammals =[]
for animal in animals:
   if (animal["group"]=="mammals"):
      mammals.append(animal)
print(mammals)

# print out the animal that has more than 7 letters

animal_with_long_name = []
for animal in animals:
   if (len(animal["name"])> 7):
      animal_with_long_name.append(animal)
print(animal_with_long_name)