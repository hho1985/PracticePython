usuario1 = input("Ingrese su nombre: ")
usuario2 = input("Ingrese su nombre: ")

ingreso1=input("%s Ingrese Piedra, Papel o Tijera "% usuario1)
ingreso2=input("%s Ingrese Piedra, Papel o Tijera "% usuario2)

def juego (eleccion1, eleccion2):
    if eleccion1 == eleccion2:
        return ("Empate")

    elif eleccion1 == "Piedra":
        if eleccion2 == "Tijera":
            return ("Piedra gana")
        else:
            return ("Papel gana")    

    elif eleccion1 == "Papel":
        if eleccion2 == "Piedra":
            return ("Papel gana")
        else:
            return ("Tijera gana")

    elif eleccion1 == "Tijera":
        if eleccion2 == "Papel":
            return ("Tijera gana")
        else: 
            return ("Piedra gana")

    else:
        return ("Seleccione Piedra, Papel o Tijera")

    
print(juego(ingreso1,ingreso2))

