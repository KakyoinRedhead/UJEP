zbozi = {
    "rohlik": 3,
    "čokolada": 75,
    "mléko": 25,
    "sýr": 45,
    "jablko": 10,
    "banán": 15,
    "káva": 120,
    "čaj": 80,
    "vejce": 50,
    "máslo": 60,
    "chleba": 30,
    "brambory": 20,
    "rýže": 45,
    "mouka": 18,
    "olej": 50,
    "těstoviny": 35,
    "cukr": 22,
    "sůl": 20,
    "paprika": 12,
    "rajče": 85
}


pocet = 0
kosik = []

while True:
    inpt = input("zadejte zboži a množství ktere chcete koupit nebo ZAPLATIT: ").strip()
    if(inpt == "ZAPLATIT"):
        break

    
