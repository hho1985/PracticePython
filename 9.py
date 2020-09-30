import random
aleatorio = random.randint(1,9)
ingreso = 0
count = 0

while ingreso != aleatorio:
    
    ingreso = int(input("Ingrese un numero aleatorio del 1 al 9: "))
    count = count+1

    if ingreso > aleatorio:
        print("Muy alto")

    elif ingreso < aleatorio:
        print ("Muy bajo")

    elif ingreso == aleatorio:
        print ("Acertaste en %s intentos" %count)
        


