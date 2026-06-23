
"""
UPIRE TEMPLATE

--- UNDERSTAND ---

    I - Inputs: list of 
    O - Outputs: the total
    C - Constraints: use a stack
    E - Edge Cases (and examples):empty list, strings,

--- PLAN ---
turn the input list into a stack, then pop each value and add it on to the previous one, 
then return the total once the list is empty
--- IMPLEMENT ---

"""

"""
At a cultural festival, multiple performances are scheduled on a single stage. 
However, due to last-minute changes, some performances need to be rescheduled or canceled. 
The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

def manage_stage_changes(changes):
    pass
Example Usage:

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
Example Output:

["A", "C", "B", "D"]
[]
["Z"]
"""



