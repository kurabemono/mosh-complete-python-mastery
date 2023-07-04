x = input("x: ")

# will cause TypeError, because x is a string
# y = x + 1

# converting x to int solves problem
y = int(x) + 1
print(f"x: {x}, y: {y}")

# Falsy values
# empty string: ""
# zero: 0
# None
