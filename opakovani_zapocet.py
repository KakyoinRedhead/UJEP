# první uloha:  vypočita prumernou delku slova v textu ze souboru 


# fibonaciho posloupnost podle n indexu

def fibo(n):

    if n < 0:
        print("čislo musí být větší než 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1


    a, b = 0, 1
    for i in range (2, n + 1):
        a, b = b, a + b
    return b
            
    
#print(fibo(5))
#print(fibo(0))
print(fibo(1))
#print(fibo(55))