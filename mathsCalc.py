import math
total = 0
addQ = ""

while (True):
    x1 = int(input("\nEnter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))
    newAddQ = input("Start (s) or end (e) addition queue? ")
    distance = math.sqrt((math.pow(x2-x1, 2))+math.pow(y2-y1, 2))
    print("Distance: ", distance)
    if (newAddQ == "s"):
        addQ = "s"
    elif (newAddQ == "e"):
        addQ = "e"

    if (addQ == "s"):
        total = total + distance
        print("Total: ", total)
    elif (addQ == "e"):
        total = total + distance
        print("Total: ", total)
        total = 0
        addQ = ""
