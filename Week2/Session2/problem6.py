"""
As a conservationist, your research center has been raising multiple endangered species and is now ready to 
reintroduce them into their native habitats. You are given two 0-indexed strings raised_species and target_species. 
The string raised_species represents the list of species available to release into the wild at your center,
 where each character represents a different species. The string target_species represents a specific sequence of species you want 
 to form and release together.

You can take some species from raised_species and rearrange them to form new sequences.

Return the maximum number of copies of target_species that can be formed by taking species from raised_species and rearranging them.

def max_species_copies(raised_species, target_species):
  pass
Example Usage:


raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2
Example Output:

1
Example 1 Explanation:
We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
We can make at most one copy of "abc", so we return 1.
Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot 
reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".

2
Example 2 Explanation:
We can make one copy of "abc" by taking the letters at indices 0, 5, and 9.
We can make a second copy of "abc" by taking the letters at indices 1, 6, and 10
At this point we are out of the letter "c" and cannot make additional copies. 
"""

def max_species_copies(raised_species, target_species):
    raised_count = {}
    target_count = {}
    track = []
    for i in raised_species:
        raised_count[i] = raised_count.get(i,0) + 1
    for i in target_species:
        target_count[i] = target_count.get(i,0) + 1
    for i in target_count:
        track.append(raised_count[i] // target_count[i])
    return min(track)

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2