num_1 = float(input("Introduzca primer numero: "))
num_2 = float(input("Introduzca segundo numero: "))
operacion = input("Introduzca que operacion quiere realizar SUMAR,RESTAR,MULTIPLICAR,DIVIDIR: ")
resultado = 0

def calculo():
    print("El resultado de", operacion, "es =", resultado, sep=" " )
    
if operacion == "SUMAR":
   resultado = num_1 + num_2
   calculo()
elif operacion == "RESTAR":
     resultado = num_1 - num_2
     calculo()
elif operacion == "MULTIPLICAR":
     resultado = num_1 * num_2
     calculo()
elif operacion == "DIVIDIR":
     resultado = num_1 / num_2
     calculo()
else:
     print("La operacion introducida es incorrecta")
     


  
