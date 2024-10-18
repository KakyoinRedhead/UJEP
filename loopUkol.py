listCisel = []

cislo = input("zadej čisla rozdelena mezerou:")

listCisel = list(map(int, cislo.split()))

print("cisla", listCisel)
def secti():
    a = 0
    for i in listCisel:
        a = a + i 
    return a

def skrati():
    a = 1
    for i in listCisel:
        a = a * i
    return a

def odecti():
    a = 0
    for i in listCisel:
        a = a - i
    return a

def vydel():
    a = 1
    for i in listCisel:
        a = a / i
    return a

metody = {
  "+": secti(),
  "*": skrati(),
  "-": odecti(),
  "/": vydel()
}


print(metody[input()])
