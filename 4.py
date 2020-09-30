numero = int(input("Ingrese un numero: "))

divisores = list(range(1,numero+1))
lista=[]

for i in divisores:
    if numero % i ==0:
        lista.append(i)
        
print (lista)