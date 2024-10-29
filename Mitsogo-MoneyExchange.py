# Given an array of denominations and a target amount, find the minimum number of notes required to reach the target amount.  (asked in Mitsogo)

# Example:

# Input: denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], target amount = 100
# Output: [50, 50]

# Input: denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], target amount = 120

# Output: [100, 20]

# Input: denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], target amount = 275

# Output: [200, 50, 20, 5]

# Input: denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], target amount = 1000

# Output: [1000]


# METHOD 1 (TC->O(n))
def minNotes(denominations, target):
    notes = []
    i = len(denominations) - 1
    while i >= 0:
        while target >= denominations[i]:
            target -= denominations[i]
            notes.append(denominations[i])
        i -= 1
    return notes
denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
target = 275
result = minNotes(denominations, target)
print(result)
# Output: [200, 50, 20, 5]


# METHOD 2 (TC->O(n))
def minNotes(denominations, target):
    notes = []
    for i in range(len(denominations) - 1, -1, -1):
        while target >= denominations[i]:
            target -= denominations[i]
            notes.append(denominations[i])
    return notes
denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
target = 275
result = minNotes(denominations, target)
print(result)
# Output: [200, 50, 20, 5]


# METHOD 3 (TC->O(n))

def minNotes(denominations, target):
    notes = []
    for i in range(len(denominations) - 1, -1, -1):
        while target >= denominations[i]:
            target -= denominations[i]
            notes.append(denominations[i])
    return notes
denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
target = 275
result = minNotes(denominations, target)
print(result)

# Output: [200, 50, 20, 5]