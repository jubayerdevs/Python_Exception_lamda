x = 6

def sample():
    try:
        if x%2 == 0:
            raise Exception("NOT ALLOWED")
            #print("NOT ALLOWED")
        # raise Exception("I will not allow even numbers")
        print(x)
    except Exception as e:
        print(e)