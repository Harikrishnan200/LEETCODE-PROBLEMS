# Sorting People Based on Multiple Criteria (Age and Name)
# Problem: Given a list of people, where each person is represented as a tuple (age, name), sort the list such that:

# The primary criterion is age (ascending).
# If two people have the same age, sort them by name (lexicographically).

#input:    people = [(30, "Alice"), (25, "Bob"), (30, "Charlie"), (20, "David")]
# Output: [(20, 'David'), (25, 'Bob'), (30, 'Alice'), (30, 'Charlie')]

from functools import cmp_to_key
def compare(person1, person2):
    if person1[0] < person2[0]:
        return -1  # Compare age
    elif person1[0] > person2[0]:
        return 1
    else:
        # If ages are the same, compare names lexicographically
        if person1[1] < person2[1]:
            return -1
        elif person1[1] > person2[1]:
            return 1
        else:
            return 0

def sort_people(people):
    return sorted(people, key=cmp_to_key(compare))

people = [(30, "Alice"), (25, "Bob"), (30, "Charlie"), (20, "David")]
print(sort_people(people))  
