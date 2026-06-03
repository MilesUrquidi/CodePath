"""
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
	pass
Example Usage

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
Example Output:

"nananananana batman!"
"batman!"
"""

def nanana_batman(x):
    res = ""
    for i in range(x):
        res += "na"
    if x > 0:
        res += " batman!"
    else: res += "batman!"
    print(res)


x = 6
nanana_batman(x)

x = 0
nanana_batman(x)