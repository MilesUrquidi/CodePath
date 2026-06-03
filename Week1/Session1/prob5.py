"""
Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

def concatenate(words):
	pass
Example Usage

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)
Example Output:

"vengeancedarknessbatman"
""
"""

def concatenate(words):
    res = ""
    for i in words:
        res += i
    print(res)

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)