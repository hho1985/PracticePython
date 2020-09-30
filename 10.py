a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

repetidos =[]

for primera in a:
    if primera in b:
        repetidos.append(primera)
    
new_repetidos=list(dict.fromkeys(repetidos)) 

print (new_repetidos)
    