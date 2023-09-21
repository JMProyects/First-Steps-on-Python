class Figura():
    
    def __init__(self, num_lados, longitud):
        self.num_lados = num_lados
        self.longitud = longitud
    
    def hallar_perimetro(self):
        return self.num_lados * self.longitud
    
piramide = Figura(4,8)        
res = piramide.hallar_perimetro()

class Usuario():
    
    def __init__(self, nombre, pin, saldo):
        self.nombre = nombre
        self.pin = pin
        self.saldo = saldo
    
class Banco():
    def __init__(self, usuarios=[]):
        self.usuarios = usuarios
        
    def autenticar(self, nombre, pin):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.pin == pin:
                    print('Estas logueado\n')
                    return True
                    
                else:
                    print('Pin incorrecto\n')
                    return False
                    
        else:
            print('El usuario no existe!\n')
            return False
            
    def mostrarUsuarios(self):
        for user in self.usuarios:
            print("Usuario: "+user.nombre+"\nPin: "+str(user.pin)+"\nSaldo: "+str(user.saldo))
    
    def mostrarSaldo(self, nombre):
        for user in self.usuarios:
            if user.nombre == nombre:
                return user.saldo
    
    def sacarDinero(self, nombre, saldo):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.saldo < saldo:
                    print('Saldo insuficiente\n')
                    break
                elif usuario.saldo >= saldo:
                    usuario.saldo -= saldo
                    print('Su nuevo saldo es: ', usuario.saldo, "\n")

usuario1 = Usuario('Jacques',9872,450)
usuario2 = Usuario('Paco',5555,200)
usuario3 = Usuario('Juan',2222,900)

banco = Banco(usuarios=[usuario1,usuario2,usuario3])

#banco.autenticar('Pepe',9872)
#banco.mostrarUsuarios()

while True:
    print('Bienvenido a Caixabank. Identifiquese:')
    print('Introduzca el nombre:')
    nombre = input()
    print('Introduzca el pin:')
    pin = int(input())
    
    if banco.autenticar(nombre, pin):
        while True:
            print('Por favor, seleccione una de estas opciones: \n 1.- Sacar dinero \n 2.- Consultar saldo \n 3.- Terminar sesión')
            opcion = input()
            if opcion == '1':
                print('Introduce la cantidad a sacar: ')
                saldo = int(input())
                banco.sacarDinero(nombre, saldo)
            elif opcion == '2':
                res = banco.mostrarSaldo(nombre)
                print('Este es su saldo actual: ', str(res) +"\n")
            elif opcion == '3':
                print('Saliendo del sistema\n')
                break
            else:
                print('Opcion incorrecta')
    
    else:
        print('Usuario no autenticado, por favor, introduza un nombre y/o pin correctos\n')
        