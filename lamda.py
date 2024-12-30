def add_one(x):
    return x + 1

#anonymous function
add_one_lambda = lambda x: x + 1
mul_one_lambda = lambda x: x ** 2

a = add_one_lambda(5)
b = add_one(5)

print(a, b)


demo = lambda x, y: x + y
demo(2, 4) //6