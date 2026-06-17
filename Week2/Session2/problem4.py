"""
In your work with a wildlife conservation database, you have two lists: 
observed_species and priority_species. The elements of priority_species are distinct, 
and all elements in priority_species are also in observed_species.

Write a function prioritize_observations() that sorts the elements of observed_species such that the 
relative ordering of items in observed_species matches that of priority_species.
 Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.

def prioritize_observations(observed_species, priority_species):
  pass
Example Usage:

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

Expected Output:

["🐯", "🐯", "🐯", "🦌", "🐘", "🦁", "🦁", "🐍", "🐻", "🐼", "🦑"]
["cardinal", "sparrow", "bluejay", "crow", "robin"]
✨ AI Hint: extend()

U: have the observed species be in the order of priority, and any leftovers are placed at the end in ascening order
P: make a new answer list, loop through observed and make a value map of how many times a species appears.
 loop through the priority and then add to that empty list the species and how many times it appears,
   then once its empty you just .extend with the leftover species from observed
"""

def prioritize_observations(observed_species, priority_species):
    final = []
    values = {}
    leftover = []
    for i in observed_species:
        values[i] = values.get(i,0) + 1
    for i in priority_species:
        final.extend([i] * values[i])
    leftovers = []
    for i in values:
        if i not in priority_species:
            leftovers.append(i)
    leftovers.sort()
    final.extend(leftovers)
    return final

    
    
observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 