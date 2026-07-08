"""
Given a list of episode durations from a podcast series, 
find the median episode length. The median is the middle value when the list is sorted. 
If the list has an even number of elements, return the average of the two middle values.

Evaluate the time and space complexity of your solution. Define your variables and provide a
 rationale for why you believe your solution has the stated time and space complexity.

  pass
Example Usage:

print(find_median_episode_length([45, 30, 60, 30, 90])) 
print(find_median_episode_length([90, 80, 60, 70, 50]))
print(find_median_episode_length([30, 10, 20, 40, 30, 50])) 
Example Output:

45
70
30.0
"""

def find_median_episode_length(durations):
    durations = sorted(durations)
    n = len(durations)
    
    mid = n // 2

    if n % 2 == 1:
        return durations[mid]
    else:
        return (durations[mid - 1] + durations[mid]) / 2

print(find_median_episode_length([45, 30, 60, 30, 90])) 
print(find_median_episode_length([90, 80, 60, 70, 50]))
print(find_median_episode_length([30, 10, 20, 40, 30, 50])) 

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
