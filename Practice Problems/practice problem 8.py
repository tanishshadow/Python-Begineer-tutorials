"""Author  : Tanish Sarmah
Date : 22/09/2020
Purpose : codewithharry practice problem 8
"""

rohanList = []


def rohanTable(n):
    """Returns a fake multiplication"""
    # Initialising fake multipliction table's list
    global rohanList

    for i in range(1, 11):

        numbers = (i * n)
        rohanList.append(numbers)
    """Generating a random number which will be added in any of rohanList's number to make
    it a fake table """

    import random
    fN = random.randint(0, n)
    np = random.choice(rohanList)
# Finding the index of the item which is same as "np"
    for index, item in enumerate(rohanList):
        if item == np:
            idx = index
            break

    rohanList.remove(np)

    rohanList.insert(idx, fN + np)

# Making a function which will generate a real multiplication table and find
#  out the error from the fake table above.


realList = []


def realTable():
    """Generates a real table and finds out the error from rohan's list"""
    global realList
    for i in range(1, 11):
        number2 = n * i
        realList.append(number2)


def faultChecker():
    """Finds and returns the worng thing in the table"""
    var = zip(realList, rohanList)
    for item in var:

        tp = item
        if tp[0] != tp[1]:
            return f"{tp[1]} is wrong in rohan's table  it should be {tp[0]}"

    else:

        return None


if __name__ == "__main__":
    n = int(input("Enter a number:\n"))

    rohanTable(n)
    realTable()
    print(f"Rohan's table : {rohanList}")
    print(f"The real table should look like {realList}")
    print(faultChecker())
