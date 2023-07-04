try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid age.")
else:
    # will be run if no exceptions were thrown
    print("No exceptions were thrown.")
finally:
    # will be run regardless if exceptions are thrown or not
    file.close()
    print("Will be run.")
