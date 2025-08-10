print("-"*24 + "POO" + "-"*24)
class MenuCafe:
    def __init__(self, position, price, style, size, origin):
        self.position = position
        self.price= price
        self.style = style
        self.size = size
        self.origin = origin
    def coffee_info(self):
        print(f"-----> Número ingresado de café: {self.position}\n"
            f"----> Precio de café: {self.price}\n"
            f"----> Estilo de café: {self.style}\n"
            f"----> Tamaño de café: {self.size}\n"
            f"----> Lugar de origen del café: {self.origin}")

def hi():
    print("-"*10 + "BIENVENIDO AL MENÚ DE CAFETERIA" + "-"*10)

coffee = []
def add_coffee():
    try:
        position =int(input("Ingrese numero de cafe que quiere ingresar: "))
        price = int(input("Ingrese el precio del cafe: "))
        style = input("Ingrese el estilo de cafe: ")
        size = input("Ingrese el tamaño del cafe: ")
        origin = input("Ingrese el lugar de origen del cafe: ")
        cafe = MenuCafe(position, price, style, size, origin)
        print(f"Cafe {style} ha sido agregado correctamente! ")
        coffee.append(cafe)
    except ValueError:
        print("Ingrese un valor valido!")
    except TypeError:
        print("Tipo de error invalido")
    except Exception as e:
        print("¡Un error inesperado ha pasado!", e)

def view_coffee():
    if not coffee:
        print("Ningun cafe ha sido agregado, ingrese uno primero.")
    else:
        print("-"*15 + "LISTA DE CAFE AGREGADOS" + "-"*15)
        for cafe in coffee:
            print(cafe.coffee_info())

def remove_coffee():
        print("-" * 15 + "ELIMINAR UN CAFE AGREGADO: " + "-" * 15)
        try:
            removed = input("Ingrese el estilo de cafe que quiere eliminar: ")
            found = False
            for cafe in coffee:
                if cafe.style == removed.lower():
                    coffee.remove(removed)
                    print("Cafe eliminado correctamente!")
                    found = True
                    break
            if not coffee:
                print("El cafe no existe!")
        except ValueError:
            print("Ingrese el valor necesario!")
        except TypeError:
            print("El valor no coincide con la peticion")
        except Exception as e:
            print("Un error inesperado ha pasado!",e)


def clean_list():
    while True:
        print("1. Si\n"
              "2. No\n")
        clean = int(input("¿Desea eliminar la lista completa ingresada?"))
        if coffee:
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
                print("Un error inesperado ha pasado!", e)
        break

def count_coffee():
    print("."*10 +"CONTADOR DE CAFE" + "."*10)
    try:
        if not coffee:
            print("No hay cafes agregados, ingrese uno primero.")
        else:
            try:
                print("1. Si\n"
                      "2. No")
                count = int(input("¿Desea verificar que cafes se repiten?: "))
                match count:
                    case 1:
                        print("Averiguando.... ")
                        for lista in coffee:
                            if lista.position == count:
                                lista.count(MenuCafe)
                                print(count)
            except ValueError:
                print("Ingrese un valor valido!")
            except TypeError:
                print("Ingrese el tipo de valor valido")
            except Exception as e:
                print("Un error inesperado ha pasado!",e)
    except ValueError:
        print("Ingrese un valor valido!")
    except TypeError:
        print("Ingrese el tipo de valor valido")
    except Exception as e:
        print("Un error inesperado ha pasado!",e)

while True:
    hi()
    try:
        print("1. Agregar cafe.\n"
              "2. Mostrar la lista de cafe completa.\n"
              "3. Eliminar cafe.\n"
              "4. Limpiar la lista de cafe.\n"
              "5. Contador de cafe.\n"
              "6. Salir.\n")
        option_user = int(input("Ingrese la opcion que desea ejecutar: "))
        match option_user:
            case 1:
                add_coffee()
            case 2:
                view_coffee()
            case 3:
                remove_coffee()
            case 4:
                clean_list()
            case 5:
                count_coffee()
            case 6:
                print("Saliendo del programa....")
                print("Gracias por usar el programa!")
                break
            case _:
                print("Ingrese una opcion valida.")
    except ValueError:
        print("Ingrese un valor valido.")
    except TypeError:
        print("Ingrese el tipo de valor valido.")
    except Exception as e:
        print("Un error inesperado ha pasado!",e)