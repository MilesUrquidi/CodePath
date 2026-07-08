"""
Given a list of episode durations from a podcast series, 
your task is to identify the longest episode. If there are multiple episodes with the maximum duration, 
return the duration of the longest episode.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

  pass
Example Usage:

print(identify_longest_episode([30, 45, 60, 45, 30]))
print(identify_longest_episode([20, 30, 40, 40, 30, 20]))  
print(identify_longest_episode([55, 60, 55, 60, 60])) 
Example Output:

60
40
60
"""

def identify_longest_episode(durations):
    return max(durations)

print(identify_longest_episode([30, 45, 60, 45, 30]))
print(identify_longest_episode([20, 30, 40, 40, 30, 20]))  
print(identify_longest_episode([55, 60, 55, 60, 60])) 