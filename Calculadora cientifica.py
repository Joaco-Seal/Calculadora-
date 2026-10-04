
import math
def calculadora():
    while True:
        print("\n Calculadora Cientifica")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Potencia")
        print("6. Raiz cuadrada")
        print("7. Seno")
        print("8. Coseno")
        print("9. Tangente")
        print("10. Logaritmo")
        print("11. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "11":
            print("Calculadora finalizada.")
            break

        if opcion == "1":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            print("Resultado:", a + b)

        elif opcion == "2":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            print("Resultado:", a - b)

        elif opcion == "3":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            print("Resultado:", a * b)

        elif opcion == "4":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))

            if b == 0:
                print("No se puede dividir entre cero.")
            else:
                print("Resultado:", a / b)

        elif opcion == "5":
            a = float(input("Base: "))
            b = float(input("Exponente: "))
            print("Resultado:", a ** b)

        elif opcion == "6":
            a = float(input("Numero: "))

            if a < 0:
                print("No se puede calcular raiz negativa.")
            else:
                print("Resultado:", math.sqrt(a))

        elif opcion == "7":
            grados = float(input("Angulo en grados: "))
            print("Resultado:", math.sin(math.radians(grados)))

        elif opcion == "8":
            grados = float(input("Angulo en grados: "))
            print("Resultado:", math.cos(math.radians(grados)))

        elif opcion == "9":
            grados = float(input("Angulo en grados: "))
            print("Resultado:", math.tan(math.radians(grados)))

        elif opcion == "10":
            a = float(input("Numero positivo: "))

            if a <= 0:
                print("El numero debe ser positivo.")
            else:
                print("Resultado:", math.log10(a))

        else:
            print("Opcion invalida.")

            
calculadora()

