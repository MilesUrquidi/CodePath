"""
The assignment statement to the top_hits_2010s variable below creates the linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. 
Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.
"""

class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
        

top_hits_2010s = SongNode("Uptown Funk")
party_rock = SongNode("Party Rock Anthem")
bad_romance = SongNode("Bad Romance")

top_hits_2010s.next = party_rock
party_rock.next = bad_romance


print_linked_list(top_hits_2010s)
