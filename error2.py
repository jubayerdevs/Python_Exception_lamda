
try:
        apples = int(input("How many apples?"))
        persons = int(input("How many persons?"))

        dist = apples / persons
        print(f"Apple per person, {dist}")

except ValueError:
        print("Please enter only numeric values")
except ZeroDivisionError:
        print("Number of persons can not be zero!")
except:
        print("Unknown error happens!")