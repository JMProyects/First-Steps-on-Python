class Productos():
    def __init__(self, tipo, titulo, cantidad, precio):
        self.tipo = tipo
        self.titulo = titulo
        self.cantidad = cantidad
        self.precio = precio
       
    def __str__(self):
        return "Tipo: " + self.tipo + "\n Titulo: " + self.titulo + "\n Cantidad: " + self.cantidad + "\n Precio: " + self.precio
    
    

class CentroComercial():
    def __init__(self, productos=[]):
        self.productos = productos
        
    def mostrarProductos(self):
        for prodKey in self.productos:
            print(prodKey, "\n")
            
    def comprarProductos(self, titulo):
        for index, producto in enumerate(self.productos):
            if producto.titulo == titulo:
                del(self.productos[index])
                print('Producto', '"',titulo,'"', 'comprado. Gracias!')
                break
        else:
            print("El producto no existe o no está disponible!")

class Alimento(Productos):
    kilos = '3kg'
    
    def __str__(self):
        return "Tipo: " + self.tipo + "\n Titulo: " + self.titulo + "\n Cantidad: " + str(self.cantidad) + "\n Kilos: " + self.kilos + "\n Precio: " + str(self.precio)
    
class Electrodomestico(Productos):
    marca = 'Samsung'
    
    def __str__(self):
        return "Tipo: " + self.tipo + "\n Titulo: " + self.titulo + "\n Cantidad: " + str(self.cantidad) + "\n Marca: " + self.marca + "\n Precio: " + str(self.precio)
    
class Moda(Productos):
    marca = 'Nike'
    talla = 'L'
    
    def __str__(self):
        return "Tipo: " + self.tipo + "\n Titulo: " + self.titulo + "\n Cantidad: " + str(self.cantidad) + "\n Marca: " + self.marca + "\n Talla: " + self.talla + "\n Precio: " + str(self.precio)
        
producto1 = Alimento('Alimento','Manzana', 5, 1.5)
producto2 = Electrodomestico('Electrodomestico','Nevera', 1, 399)
producto3 = Moda('Moda','Camiseta', 2, 10)

#otra forma de hacerlo
#prd = Productos('Alimento','Manzana', 5, 1.5)

listaProductos = []
listaProductos.append(producto1)
listaProductos.append(producto2)
listaProductos.append(producto3)

centroComercial1 = CentroComercial(listaProductos)

#Otra forma de hacerlo
#c2 = CentroComercial(productos=[producto1, producto2, producto3])

#centroComercial1.mostrarProductos()

#Otra forma de hacerlo
#c2.mostrarProductos()   
    
while True:
    print('Bienvenido a SuperMarket!. Por favor, seleccione una de las siguientes opciones: \n1.- Consultar productos \n2.- Vender productos \n3.- Terminar sesión')
    opcion = input()
    
    if opcion == '1':
        print('\nEstos son todos nuestros productos disponibles: \n')
        centroComercial1.mostrarProductos()
    
    elif opcion == '2':
        print('\nProductos disponibles: \n')
        centroComercial1.mostrarProductos()
        print('\nSeleccione un producto que quiera comprar')
        comprar = input()
        centroComercial1.comprarProductos(comprar)
        
    elif opcion == '3':
        print('Saliendo del sistema...')
        break
    
    
    

