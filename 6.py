from datetime import datetime

# Get user input
current_age = input("What is your current age? ")
retirement_age = input("At what age would you like to retire? ")

# Perform calculations
years_left = (int(retirement_age) - int(current_age))
current_year = datetime.now().year
retirement_year = current_year + years_left

# Generate output
output = (f"You have {years_left} years left until you can retire.\n"
          f"It's {current_year}, so you can retire in {retirement_year}.")

print(output)

