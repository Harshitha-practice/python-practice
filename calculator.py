a=int(input('a: '))
b=int(input('b: '))
print('1.Addition \n2.Substraction \n3.Multiplication \n4.Division')
ch=input('Enter your choice: ')
if ch=='1':
    print('Addition of two i/p numbers: {}'.format(a+b))
elif ch=='2':
    print('Substraction of two i/p numbers: {}'.format(a-b))
elif ch=='3':
    print('Multiplication of two i/p numbers: {}'.format(a*b))
elif ch=='4':
    print('Division of two i/p numbers: {}'.format(a/b))
else:
    print("Invalid Choice")