def greet():
  print("hello")

greet()

def greet2(name):
  print("hello,", name)

greet2("Alan")
greet2("Mario")
greet2("Luigi")

def add(a, b):
  # you can return from a function
  # and do anything that you want with it
  return a+b

print(add(10, 2))