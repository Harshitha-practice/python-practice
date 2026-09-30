a=int(input("a: "))
if a % 2 == 0:
    print('Even')
elif a%1 == 0 and a%a == 0:
    print('Prime')
else:
    print('Odd')