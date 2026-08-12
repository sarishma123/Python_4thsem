x=100
def func():
    x=55
    print("inside function",x)
func()
print("outside the function",x)

x=100
def func():
    global x
    x=55
    print("inside function",x)
print("outside function before editing",x)
func()
print("outside function after editing",x)

# task
x=20
def process():
    x=20
    print(x)
process()

# wap showing the manupulation of global variable

