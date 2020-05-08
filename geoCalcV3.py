#Dear future me: remember that when using 'or' in a conditional statement, you need to rewrite the variable (mode == 'a' or mode == 'b' NOT mode == 'a' or 'b') becuase what happens when you don't rewrite the variable is that Python treats 'b' as it's own condition which returns true because 'b' is not 0 and anything other than 0 is considered to be true and this is why the code was running in the conditional statements when the conditions weren't met.
import math
total = 0 #Var used to store the aggregated distance values of lines
clearTotal = "" #If this is set to anything but '', the total value will be reset
print("Welcome to version 3.0 of my math calculator!")
print("a. Distance Formula/Perimeter Finder\nb. Area Finder\nc. Midpoint Finder")
mode = input("Which calc would you like to use?\n(type 'a', 'b', or 'c' and then press Enter): ")
while (mode != 'a' and mode != 'A' and mode != 'b' and mode != 'B' and mode != 'c' and mode != 'C'):
  mode = input("Oops, please type 'a', 'b', or 'c' and then press enter: ")
while True:
  while (mode == 'a' or mode == 'A'):
    error = True
    errorMessage = False
    while (error):
      if (errorMessage):
        print("Oops, it looks like you entered something other than a number for one of the inputs; Please try again")
      x1 = input("\nEnter x1: ")
      y1 = input("Enter y1: ")
      x2 = input("Enter x2: ")
      y2 = input("Enter y2: ")
      try:
        float(x1)
        float(y1)
        float(x2)
        float(y2)
      except:
        errorMessage = True
      else:
        error = False #This will cause the input loop to be exited
    clearTotal = input("Reset total value? (type any character, else, press Enter): ")
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    distance = math.sqrt((math.pow(x2-x1, 2))+math.pow(y2-y1, 2))
    print("Distance: ", distance)
    #'Total' functionality
    if (clearTotal != ''):
      total = 0
    total = total + distance
    print("Total: ", total)

  while (mode == 'b' or mode == 'B'):
    error = True
    errorMessage = False
    while (error):
      if (errorMessage):
        print("Oops, it looks like you entered something other than a number for one of the inputs; Please try again")
      print("Enter the endpoints of the base")
      bx1 = input("Enter bx1: ")
      by1 = input("Enter by1: ")
      bx2 = input("Enter bx2: ")
      by2 = input("Enter by2: ")
      try:
        float(bx1)
        float(by1)
        float(bx2)
        float(by2)
      except:
        errorMessage = True
      else:
        error = False #This will cause the input loop to be exited
    error = True
    errorMessage = False
    while (error):
      if (errorMessage):
        print("Oops, it looks like you entered something other than a number for one of the inputs; Please try again")
      print("\nEnter the endpoints of the height")
      hx1 = input("Enter hx1: ")
      hy1 = input("Enter hy1: ")
      hx2 = input("Enter hx2: ")
      hy2 = input("Enter hy2: ")
      try:
        float(hx1)
        float(hy1)
        float(hx2)
        float(hy2)
      except:
        errorMessage = True
      else:
        error = False #This will cause the input loop to be exited
    sides = input("\n\nHow many sides does this figure have (3/4)?: ")
    while (sides != '3' and sides != '4'):
      sides = input("Please type '3' or '4': ")
    bx1 = float(bx1)
    by1 = float(by1)
    bx2 = float(bx2)
    by2 = float(by2)
    hx1 = float(hx1)
    hy1 = float(hy1)
    hx2 = float(hx2)
    hy2 = float(hy2)
    base = math.sqrt((math.pow(bx2-bx1, 2))+math.pow(by2-by1, 2))
    height = math.sqrt((math.pow(hx2-hx1, 2))+math.pow(hy2-hy1, 2))
    if (sides == "3"):
      print("\nArea: ", 0.5*(base * height))
    elif (sides == "4"):
      print("\nArea: ", (base * height))
  while (mode == 'c' or mode == 'C'):
    print("\ne. Calculate midpoint with two endpoints\nf. Calculate endpoint with the midpoint and on endpoint")
    midpointMode = ''
    while (midpointMode != 'e' and midpointMode != 'E' and midpointMode != 'f' and midpointMode != 'F'):
      midpointMode = input("Type 'e' or 'f' and press enter to choose mode: ")
    error = True
    errorMessage = False
    while (error):
      if (errorMessage):
        print("Oops, it looks like you entered something other than a number for one of the inputs; Please try again")
      print("\nEndpoint A")
      x1 = input("Enter x1: ")
      y1 = input("Enter y1: ")
      if (midpointMode == 'e' or midpointMode == 'E'):
        print("\nEndpoint B")
      else:
        print("\nMidpoint")
      x2 = input("Enter x2: ")
      y2 = input("Enter y2: ")
      try:
        float(x1)
        float(y1)
        float(x2)
        float(y2)
      except:
        errorMessage = True
      else:
        error = False #This will cause the input loop to be exited
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    if (midpointMode == 'e' or midpointMode == 'E'):
      midpointX = (x1 + x2)/2
      midpointY = (y1 + y2)/2
    else:
      if (x1 < x2):
        midpointX = x2 + math.fabs(x1-x2)
      elif (x1 > x2):
        midpointX = x1 - x2

      if (y1 < y2):
        midpointY = y2 + math.fabs(y1-y2)
      elif (y1 > y2):
        midpointY = y1 - y2
    print("Midpoint: (", midpointX, ",", midpointY, ")")
    #What if y1 and y2 are equal????
