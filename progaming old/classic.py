'''
 askk user for 3 things
 a number
 an thing
 and a attribute

 then print:
 jij bent een dier met nummer poten
'''
attribute = input('attribute: ')
thing = input('thing: ')
number = input('random number: ')

number = int(number)
number = number ** 2
if number < 100:
    print('must have large brain')
number = str(number)


print(
        'you are a',
         attribute,
         thing,
         'with',
         number,
         'braincells'
)
