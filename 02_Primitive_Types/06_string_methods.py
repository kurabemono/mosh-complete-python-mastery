course = "python programming"

# convert to ALL CAPS
print(course.upper())  # PYTHON PROGRAMMING

# original string is unaffected
print(course)  # python programming

# convert to Title Case
print(course.title())  # Python Programming

# string leading and trailing whitespace
text = "  programming"
print(text.strip())  # programming

# find index of string
print(course.find("pro"))  # 9

# replace string
print(course.replace("p", "j"))  # jython jrogramming

# determine existence of string
print("pro" in course)  # True
print("swift" not in course)  # True
