"""
You are given a 0-indexed integer array species_populations of even length, 
where each element represents the population of a particular species in a wildlife reserve.

As long as species_populations is not empty, you must repetitively:

Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.

For example, the average of 200 and 300 is (200+300)/2=250.

Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum population, any can be removed.

def distinct_averages(species_populations):
  pass
Example Usage:

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 
Example Output:

2
Example 1 Explanation:
1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.

1
Example 2 Explanation:
There is only one average to be calculated after removing 1 and 100, 
so we return 1.

"""

def distinct_averages(species_populations):
    a = 0
    b = 0
    distinct = set()
    while species_populations:
            a = min(species_populations)
            b = max(species_populations)
            avg = (a + b)/2
            distinct.add(avg)
            species_populations.remove(a)
            species_populations.remove(b)
    return len(distinct)
        
species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 