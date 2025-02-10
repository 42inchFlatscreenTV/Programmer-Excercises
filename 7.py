length = input("What is the length of the room in feet? ")
width = input("What is the width of the room in feet? ")

print(f"You entered dimensions of {length} feet by {width} feet.\n"
      f"The area is ")

sqrfeet = (int(length) * int(width))
sqrmeters = (int(sqrfeet) * 0.09290304)

print(f"{sqrfeet} square feet\n"
      f"{sqrmeters} square meters")