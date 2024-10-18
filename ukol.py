a,b,c = input('Zadej a, b, c: ').split(',')

a,b,c = map(float,  [a,b,c])

D = b*b - 4*a*c

if D<0:
    print("Nemá reealný kořen")
elif 0==D:
    x = - b / (2*a)
    print(f'Kořen je {x=}')
else:
    sqrtD = D ** .5
    x1 = (-b + sqrtD) / (2*a)
    x2 = (-b + sqrtD) / (2*a)
    print(f'Kořenjsou {x1=}, {x2= }')

