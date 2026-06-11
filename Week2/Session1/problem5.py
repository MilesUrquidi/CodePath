"""
As part of the festival, attendees cast votes for their favorite set.
 Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the highest number of votes.
   If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    pass
Example Usage:

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
Example Output:

SZA
Ethel Cain
Note: SZA and Ethel Cain would both be acceptable answers for the second example
✨ AI Hint: Frequency Maps

"""

def best_set(votes):
    vote_count = {}
    for i in votes:
        artist = votes[i]
        vote_count[artist] = vote_count.get(artist,0) + 1
    winner = max(vote_count, key=vote_count.get)
    return winner


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1240: "Ethel Cain"
}

print(best_set(votes1))
print(best_set(votes2))