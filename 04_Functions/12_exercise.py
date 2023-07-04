def fizz_buzz(number):
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0

    if is_divisible_by_3:
        if is_divisible_by_5:
            return "FizzBuzz"
        return "Fizz"
    if is_divisible_by_5:
        return "Buzz"
    return number


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))
