    #"a) functions with no argument and no retuen type"



def addition():
    a = 12
    b = 89
    print("addition=", (a+b))


def substraction():
    a = 9
    b = 45
    print("Substraction=", (a-b))


addition()
substraction()

    # function defined

def addition(a, b):
    print("addition=", (a + b))


addition(89,56)
addition(89,6)

   #"d) functions with argument and return type"

    # function defined

def addition(a, b):
 return a + b

print("addition=", addition(89, 56))
print("addition=", addition(89, 6))

    #"c) functions with no argument and return type"

    # function defined

def addition():
  return 89+56


print("addition=", addition())
print("addition=", addition())