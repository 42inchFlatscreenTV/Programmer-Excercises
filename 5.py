#Prompts the user for two numbers
x = input("What is the first number? ")
y = input("What is the second number? ")

sum_result = x + y
difference = (int(x) - int(y))
product = (int(x) * int(y))
quotient = (int(x) / int(y)) if y != 0 else "Undefined"

# Display results
print(f"{x} + {y} = {sum_result}")
print(f"{x} - {y} = {difference}")
print(f"{x} * {y} = {product}")
print(f"{x} / {y} = {quotient}")