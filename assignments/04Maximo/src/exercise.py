def main():
    #escribe tu código abajo de esta línea
    pass
num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))
num3 = int(input("Escribe el tercer número: "))


if (num1>num2) and (num1>num3):
	print(num1)
elif (num2>num1) and (num2>num3):
	print (num2)
elif (num3>num1) and (num3>num2):
	print(num3)
    
if __name__=='__main__':
    main()
