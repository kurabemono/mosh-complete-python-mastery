from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code:", timeit(code1, number=10000))
print("second code:", timeit(code2, number=10000))
