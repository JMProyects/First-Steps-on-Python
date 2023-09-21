class Libreria():
    def __init__(self, libros=[]):
        self.libros = libros
        
    def mostrarLibros(self):
        for libro in self.libros:
            print('Titulo:', libro.titulo, "\n Autor:",libro.autor,"\n Año:",libro.año, "\n")
    
    def eliminarLibro(self, titulo):
        for index, libro in enumerate(self.libros):
            if libro.titulo == titulo:
                del(self.libros[index])
        
    
class Libro():
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    

#programa main

libro1 = Libro('Libro1','Autor1','2001')
libro2 = Libro('Libro2','Autor2','2002')
libro3 = Libro('Libro3','Autor3','2003')
libro4 = Libro('Libro4','Autor4','2004')
libro5 = Libro('Libro5','Autor5','2005')
    
libreria1 = Libreria(libros=[libro1,libro2,libro3,libro4,libro5])

while True:
    print('Bienvenido a la biblioteca online. Seleccione una opcion: \n1.- Consultar libros \n2.- Vender libros \n3.- Terminar sesión')
    opcion = input()
    
    if opcion == '1':
        print('Estos son los libros actuales:\n')
        libreria1.mostrarLibros()
        
    elif opcion == '2':
        print('Escriba el titulo del libro que desee vender:\n')
        libreria1.mostrarLibros()
        libro = input()
        libreria1.eliminarLibro(libro)
        
    elif opcion == '3':
        print('Saliendo del sistema')
        break
    else:
        print('opcion incorrecta!')
    
        