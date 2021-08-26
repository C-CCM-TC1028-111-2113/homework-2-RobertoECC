def main():
    # Escribe el código adecuado para completar el programa
    pass

x= int(input("Introduce el primer número: "))
y= int(input("Introduce el segundo número: "))
z= int(input("Introduce el tercer número: "))

if (x<y>z) and (x>z):
	print("{}\n{}\n{}".format(z, x, y))
elif (x<y>z) and (z>x):
	print("{}\n{}\n{}".format(x, z, y))
elif (y<x>z) and (y>z):
	print("{}\n{}\n{}".format(z, y, x))
elif (y<x>z) and (y<z):
	print("{}\n{}\n{}".format(y, z, x))
elif (x<z>y) and (x>y):
	print("{}\n{}\n{}".format(y, x, z))
elif (x<z>y) and (x<y):
	print("{}\n{}\n{}".format(x, y, z))

if __name__=='__main__':
    main()
