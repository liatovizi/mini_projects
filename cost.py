"""Calculate the total cost of tile it would take to cover a floor plan of width and height,
 using a cost entered by the user."""

width = float(input("Width of floor: "))
length = float(input("Length of floor: "))
cost = float(input("Cost of Tile: "))

print("Cost to tile a %.2f x %.2f floor is: $%.2f" % (width, length, width * length * cost))


