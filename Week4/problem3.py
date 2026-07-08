"""
You are given a list of episode lengths from a podcast series. 
Your task is to determine which episode length occurs most frequently. 
If there are multiple lengths with the same highest frequency, return the smallest episode length.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def most_frequent_length(episode_lengths):
  pass
Example Usage:

print(most_frequent_length([30, 45, 30, 60, 45, 30])) 
print(most_frequent_length([20, 20, 30, 30, 40, 40, 40])) 
print(most_frequent_length([50, 60, 70, 80, 90, 100]))
Example Output:

30
40
50
"""

def most_frequent_length(episode_lengths):
    tracker = {}

    for length in episode_lengths:
        tracker[length] = tracker.get(length, 0) + 1

    return max(tracker, key=tracker.get)

print(most_frequent_length([30, 45, 30, 60, 45, 30])) 
print(most_frequent_length([20, 20, 30, 30, 40, 40, 40])) 
print(most_frequent_length([50, 60, 70, 80, 90, 100]))