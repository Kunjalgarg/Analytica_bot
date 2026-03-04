first=int(input('enter starting number:'))
second=int(input('enter second number:'))
no=int(input('How many Fibonacci numbers you want to display:'))
if no<=0:
    print('Please enter positive integer:')

else:
    print(first)
    print(second)
    for i in range(2,no):
        third=first+second
        first=second
        second=third
        print(third)
print('---------------------------------------------------')
