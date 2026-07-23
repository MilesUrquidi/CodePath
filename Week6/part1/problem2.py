"""
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. Define your variables and provide a rationale 
for why you believe your solution has the stated time and space complexity.
"""

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    freq_map = {}
    current = playlist

    while current:
        freq_map[current.artist] = freq_map.get(current.artist,0) + 1
        current = current.next
    return freq_map


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))