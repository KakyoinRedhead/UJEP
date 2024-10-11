import math as math 

### Vypočet Přepony ###

a = int(input("zadej stranu a:"))
b = int(input("zadej stranu b:"))

def vypocitejPreponu(a, b):
    return math.sqrt(a**2 + b**2)
    

print("prepona je: " + str(vypocitejPreponu(a,b)))

### Pravoúhlý T ###

A = int(input("zadej stranu A pro zjištění jestli je trojuhelník pravouhlý:"))
B = int(input("zadej stranu B pro zjištění jestli je trojuhelník pravouhlý:"))
C = int(input("zadej stranu C pro zjištění jestli je trojuhelník pravouhlý:"))

def zjistiUhel(A, B, C):
    arry = [A, B, C]
    arry.sort()
    if(arry[2]**2 == arry[0]**2 + arry[1]**2):
        print("Trojuhelník je pravoúhly")
    else:
        print("není pravoúhlý")

zjistiUhel(A,B,C)

### LoTR ###

Fr = 'Frodo'
FrAge = 50

Gd = 'Gandalf'
GdAge = 2000

Sm = 'Sam'
SmAge = 38

nejstarsi_vek = max(FrAge, GdAge, SmAge)  

if (nejstarsi_vek == FrAge):
    nejstarsi = Fr
elif (nejstarsi_vek == SmAge):
    nejstarsi = Sm
elif (nejstarsi_vek == GdAge):
    nejstarsi = Gd


print(f'{Fr} is {FrAge} and {Gd} is {GdAge}.')
print(f'{Gd if FrAge<GdAge else Fr} is older and therefore wiser.')
print(f'The oldest one is {nejstarsi} who is {nejstarsi_vek} years old.')

### Automat ###

jmeno = input("zadejte jméno: ")
vek = int(input("zadejte věk: "))
