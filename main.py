import os
ciclistas = []

def menu():

    print("1. Agrgar lista")
    print("2. mostrar ciclista")
    print("3. Editar ciclistas")
    print("4. Eliminar ciclistas")
    print("5. Salir")

def ingresar():
    nombre = input("Ingrese el nombre: ")
    edad = input("ingrese la edad: ")
    pais = input("ingrese el pais: ")
    equipo = input("ingrese el equipo: ")
    tiempo = int(input("ingrese el tiempo: "))
    codigo = len(ciclistas) + 1
    ciclista = {
        "nombre":nombre,
        "edad": edad,
        "pais": pais,
        "equipo":equipo,
        "tiempo":tiempo,
        "codigo":codigo
    }
    ciclistas.append(ciclista)

def lista():
    for ciclista in ciclistas:
        print(f"El codigo del ciclista es {ciclista['codigo']}")
        print(f"El nombre del ciclista es {ciclista['nombre']}")
        print(f"La edad del ciclista es {ciclista['edad']}")
        print(f"El pais del ciclista es {ciclista['pais']}")
        print(f"El equipo del ciclista es {ciclista['equipo']}")
        print(f"El tiempo del ciclista es {ciclista['tiempo']}")


def editar():
    codigo = int(input("Ingrese el codigo del ciclista para editar: "))
    i = 0
    for ciclista in ciclistas:

        if(codigo == ciclista['codigo']):
            print(f"El tiempo actual es: {ciclista['tiempo']}")
            tiempo = int(input("Ingrese el nuevo tiempo del ciclista: "))
            ciclista["tiempo"] = tiempo
            pregunta = input("Deseas continuar ")
            break
        i= i + 1
def borrar():
    codigo = int(input("Ingrese el codigo del ciclista a borrar: "))
    i = 0
    for ciclista in ciclistas:
        if(codigo == ciclista['codigo']):
            ciclistas.remove(ciclista)
            print(f"El ciclista ingresado a sido borrado correctamente {ciclista['nombre']}")
            pregunta = input("Deseas continuar ")
            break
        i =+1           
    



while True:
    menu()

    respuesta = input("ingrese una de las opciones del menu :")

    match respuesta:

        case "1":
            ingresar()
        case "2":
            lista()
        case "3":
            editar()

        case "4":
            borrar()
        case "5":
            break
        case _:
            print("No existe esta opcion"+ respuesta)
    
    input("de enter para continuar")
    os.system("cls")