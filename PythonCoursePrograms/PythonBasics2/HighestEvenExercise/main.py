# Highest Even Exercise

def highest_even(li):
    highest = 0
    for item in li:
        if item % 2 == 0 and item > highest:
            highest = item
    return highest

print(highest_even([10,2,3,4,8,11]))
