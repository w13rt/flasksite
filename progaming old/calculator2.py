# calculator 2.0
def add(a, b):
    return a + b

def substract(a, b):
    return a -b

def times(a, b):
    return a * b

def divide(a, b):
    return a / b

def usrin():
    a = input('a = ')
    b = input('b = ')
    a = float(a)
    b = float(b)
    return a, b

print(
       'What do you want to do? ',
       '1: add ',
       '2: substract ',
       '3: multiply ',
       '4: divide ',
       sep='\n'
)

selection = input()
if selection == '1':
    print('you want to add a to b!')
    a, b = usrin()
    result = add(a, b)
    print('The result=', result)

elif selection == '2':
    print('you want to substract a from b!')
    a, b = usrin()
    result = substract(a, b)
    print('The result=', result)

elif selection == '3':
    print('you want to multiply a with b!')
    a, b = usrin()
    result = times(a, b)
    print('The result=', result)

elif selection == '4':
    print('you want to divide a by b!')
    a, b = usrin()
    result = divide(a, b)
    print('The result=', result)

else:
    print('haha idk')