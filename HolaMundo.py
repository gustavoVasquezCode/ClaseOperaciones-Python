# Crear un programa en python donde se realice operaciones aritmeticas basicas
# Cada operacion llevara su propio metodo y al final habra un metodo principal
# con un menu donde podamos ejecutar algun metodo
# Ejemplo:
#           1. Ingresar numero
#           2. Sumar
#           3. Restar
#           4. Multiplicar
#           5. Dividir
#           6. Salir

class Operaciones:
    primerNumero = 0
    segundoNumero = 0

    def ingresarNumeros(self):
        ingresoNumero1 = True
        ingresoNumero2 = True
        while ingresoNumero1:
            try:
                self.primerNumero = int(input("Ingrese el primer valor: "))
            except ValueError:
                print("\n¡Vaya! Ingreso un caracter, debe ser un numero. Try again.")
            else:
                ingresoNumero1 = False

        while ingresoNumero2:
            try:
                self.segundoNumero = int(input("Ingrese el segundo valor: "))
            except ValueError:
                print("\n¡Vaya! Ingreso un caracter, debe ser un numero. Try again.")
            else:
                ingresoNumero2 = False

    def suma(self):
        suma = 0
        print("\n*************** Suma ***************")
        suma = self.primerNumero + self.segundoNumero
        print("La suma es: ", suma)

    def resta(self):
        resta = 0
        print("\n*************** Resta ***************")
        resta = self.primerNumero - self.segundoNumero
        print("La resta es: ", resta)

    def multiplicacion(self):
        mult = 0
        print("\n*************** Multiplicacion ***************")
        mult = self.primerNumero * self.segundoNumero
        print("La multiplicacion es: ", mult)

    def division(self):
        division = 0
        print("\n*************** Division ***************")
        try:
            division = self.primerNumero / self.segundoNumero
        except ZeroDivisionError:
            print("\nUn error, el segundo numero debe ser mayor a cero.")
            print("La division es: 0")
        else:
            print("La division es: ", division)

def pedirNumeroEntero():
    ingresoOpcion = True
    opc = 0
    while ingresoOpcion:
            try:
                opc = int(input("Digite una opcion y de enter: "))
            except ValueError:
                print("\n¡Vaya! Ingreso un caracter, debe ser un numero. Try again.")
            else:
                ingresoOpcion = False
    return opc

def main():
    ejecutandoPrograma = True
    opcion = 0
    obj1 = Operaciones()
    while ejecutandoPrograma:
        print("\n*************** Operaciones basicas **************")
        print("Elija una opcion: \n\t1. Ingresar numeros \n\t2. Suma \n\t3. Resta")
        print("\t4. Multiplicacion \n\t5. Division \n\t6. Salir")
        opcion = pedirNumeroEntero()

        if (opcion == 1):
            obj1.ingresarNumeros()
        elif (opcion == 2):
            obj1.suma()
        elif (opcion == 3):
            obj1.resta()
        elif (opcion == 4):
            obj1.multiplicacion()
        elif (opcion == 5):
            obj1.division()
        elif (opcion == 6):
            ejecutandoPrograma = False
        else:
            print("\nERROR. La opcion que ingreso no existe")

main()