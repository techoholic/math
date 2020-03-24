import math
total = 0
addQ = ""
print("Welcome to my math calculator!")
print("a. Distance Formula\nb. Area Finder")
mode = input("Which calc would you like to use? ")
while True:
    while (mode == "a"):
        x1 = input("\nEnter x1: ")
        if (x1 == "b"):
            mode == "b"
            break
        else:
            x1 = int(x1)
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
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
    while (mode == "b"):
        sides = input("\n\nHow many sides does this figure have (3/4)? ")
        print("Enter the endpoints of the base")
        bx1 = input("Enter x1: ")
        if (bx1 == "a"):
            mode == "a"
            break
        else:
            bx1 = int(bx1)
        by1 = int(input("Enter y1: "))
        bx2 = int(input("Enter x2: "))
        by2 = int(input("Enter y2: "))
        print("\nEnter the endpoints of the height")
        hx1 = int(input("Enter x1: "))
        hy1 = int(input("Enter y1: "))
        hx2 = int(input("Enter x2: "))
        hy2 = int(input("Enter y2: "))
        base = math.sqrt((math.pow(bx2-bx1, 2))+math.pow(by2-by1, 2))
        height = math.sqrt((math.pow(hx2-hx1, 2))+math.pow(hy2-hy1, 2))
        if (sides == "3"):
            print("\nArea: ", 0.5*(base * height))
        elif (sides == "4"):
            print("\nArea: ", (base * height))
