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
        name =input("Ingrese El nombre del cafe que quiere agregar: ")
        price = int(input("Ingrese el precio del cafe: "))
        style = input("Ingrese el estilo de cafe: ")
        size = input("Ingrese el tamaño del cafe: ")
        origin = input("Ingrese el lugar de origen del cafe: ")
        cafe = MenuCafe(name, price, style, size, origin)
        print(f"Cafe {name} ha sido agregado correctamente! ")
        coffee.append(cafe)
    except ValueError:
        print("Ingrese un valor valido!")
    except TypeError:
        print("Tipo de error invalido")
    except Exception as e:
        print("¡Un error inesperado ha pasado!")
