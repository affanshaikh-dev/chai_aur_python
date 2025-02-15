username = "chaiaurcode"

def func(): 
    # username = 'chai'
    print(username)

print(username)
func()

x = 99

# def func2(y):
#     z = x + y
#     return z

# print(func2(1))

# def func3():
#     global x
#     x = 12
# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2

my_res = f1()
print(my_res)

my_res()

def chai_coder(n):
    def actual(x):
        return x ** n
    return actual

f = chai_coder(2)
g = chai_coder(3)

print(f(3))
print(g(3))

print(g)