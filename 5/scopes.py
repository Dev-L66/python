#  global variable
username = "John Doe"

def func():
#  username = "Bob"
 print(username)

func()

print(username)

x = 99

def func2(y):
   z = x + y
   return z

result = func2(1)
print(result)


def func3():
  global x
  x = 88
func3()
print(x)


x = 77

def f1():
  x = 88
  def f2():
    y = 66
    print("from inside f2",x)
  return f2
result = f1()

result()


def hello(n):
  def hello2(x):
    return x ** n
  return hello2

f = hello(2)
g = hello(3)

print(f(3))