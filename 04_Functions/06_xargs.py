def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


print(multiply(2, 3, 4, 5))
