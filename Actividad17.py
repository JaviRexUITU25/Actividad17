print("-"*10 + "POO" + "-"*10)
class MenuCafe:
    def __init__(self, name, price, style, size, origin):
        self.name = name
        self.price= price
        self.style = style
        self.size = size
        self.origin = origin
    def coffee_info(self):
        print(f"Nombre: {self.name} - Precio: {self.price}-  Estilo: {self.style}- Tamaño: {self.size}- Lugar de origen: {self.origin} ")

def saludo():
    print("-"*10 + "BIENVENIDO AL MENU DE CAFETERIA" + "-"*10)

coffee = []
def addcoffee():
    try:
        name =input("Ingrese El nombre del cafe que quiere agregar: ").upper()
        price = int(input("Ingrese el precio del cafe: "))
        style = input("Ingrese el estilo de cafe: ").upper()
        size = input("Ingrese el tamaño del cafe: ").upper()
        origin = input("Ingrese el lugar de origen del cafe: ").upper()
        cafe = MenuCafe(name, price, style, size, origin)
        print(f"Cafe {name} ha sido agregado correctamente! ")
        coffee.append(cafe)
    except ValueError:
        print("Ingrese un valor valido!")
    except TypeError:
        print("Tipo de error invalido")
    except Exception as e:
        print("¡Un error inesperado ha pasado!")

def viewcoffee():
    if not viewcoffee() in coffee:
        print("Ningun cafe ha sido agregado, ingrese uno primero.")
    else:
        print("-"*15 + "LISTA DE CAFE AGREGADOS" + "-"*15)
        i = 1
        for cafe in coffee:
            print(f"{i}." , end= "")
            cafe.coffee_info()
            i +=1
        print()

def removecoffee():
    print("-"*15 + "ELIMINAR UN CAFE AGREGADO: " + "-"*15)
    if not removecoffee() in coffee:
        print("Ninguna cafe ha sido agreagdo, ingrese uno primero.")
    else:
        try:
            removed = input("Ingrese el nombre del cafe que quiere eliminar: ").upper()
            for cafe in coffee:
                if cafe.name.lower() == removed.lower():
                    coffee.remove(MenuCafe)
                    break
        except ValueError:
            print("Ingrese el valor necesario!")
        except TypeError:
            print("El valor no coincide con la peticion")
        except Exception as e:
            print("Un error inesperado ha pasado!")


def cleanlist():
    while True:
        print("1. Si\n"
              "2. No")
        clean = int(input("¿Desea eliminar la lista completa ingresada?"))
        if not clean in coffee:
            print("Ningun cafe ha sido agregado, ingrese uno primero.")
        else:
            try:
                match clean:
                    case 1:
                        print("Eliminando la lista de cafes...")
                        coffee.clear()
                        print("La lista ha sido eliminada correctamente!")
                    case 2:
                        print("Volviendo al menu...")
                    case _:
                        print("Ingrese una opcion valida")
            except ValueError:
                print("-"*15 + "Valor erroneo!" + "-"*15)
            except TypeError:
                print("-"*15 + "Tipo de error invalido" + "-"*15)
            except Exception as e:
                print("Un error inesperado ha pasado!")
        break

def contarcafe():

