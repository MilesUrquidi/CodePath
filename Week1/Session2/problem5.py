"""
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
	pass
Example Usage

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
Example Output:

2
4

u: tiger starts at 1, then depending on what the word is you either add 1 or subtract 1, if its bouncy and flouncy you add 1, trouncy and pouncy subtract 1
p: just check each word in the string and depending on what it is adjust the number tiger, then return it at the end
"""
def final_value_after_operations(operations):
    tigger = 1
    for i in operations:
        if i == "bouncy" or i == "flouncy":
            tigger = tigger + 1
        elif i == "trouncy" or i == "pouncy":
            tigger = tigger - 1
    print(tigger)

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)