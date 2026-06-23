"""
You are organizing a cultural festival and have two performance schedules,
 schedule1 and schedule2, each represented by a string where each character corresponds to a
performance slot. Merge the schedules by adding performances in alternating order, starting with schedule1. 
If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.

Return the merged performance schedule.

def merge_schedules(schedule1, schedule2):
    pass
Example Usage:

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 
Example Output:

apbqcr
apbqrs
apbqcd
💡Hint: Two Pointer Technique
"""

def merge_schedules(schedule1, schedule2):
    left, right = 0, 0
    merged = []

    while left < len(schedule1) and right < len(schedule2):
        merged.append(schedule1[left])
        merged.append(schedule2[right])
        left += 1
        right += 1

    merged.append(schedule1[left:])
    merged.append(schedule2[right:])

    return "".join(merged)



print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 