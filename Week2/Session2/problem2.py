"""
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species.
 Each character in this string denotes a different endangered species. 
 You also have a record of all observed species in a particular region, represented by the string observed_species. 
 Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.

def count_endangered_species(endangered_species, observed_species):
    pass
Example Usage:

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  
Example Output:

3 # `a` and `A` are endangered species. `a` appears once, and `A` twice.
0
✨ AI Hint: Introduction to sets
"""

def count_endangered_species(endangered_species, observed_species):
    tally = 0
    check = set(endangered_species)
    for species in observed_species:
        if species in check:
            tally += 1
    return tally
  

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  