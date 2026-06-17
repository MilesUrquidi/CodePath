"""
You are given a string ecosystem_data that consists of digits and lowercase English letters. 
The digits represent the observed counts of various species in a protected ecosystem.

You will replace every non-digit character with a space. For example, "f123de34g8hi34" will become " 123 34 8 34".
 Notice that you are left with some species counts that are separated by at least one space: "123", "34", "8", and "34".

Return the number of unique species counts after performing the replacement operations on ecosystem_data.

Two species counts are considered different if their decimal representations without any leading zeros are different.

def count_unique_species(ecosystem_data):
  pass
Example Usage:

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))
Example Output:

3
2
1
"""

def count_unique_species(ecosystem_data):
    newstr = ""
    res = []
    for i in ecosystem_data:
        if i.isdigit():
            newstr += i
        else:
            newstr += " "
    parts = newstr.split()
    for i in parts:
        res.append(int(i))
    total = set(res)
    return len(total)
        
ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))
