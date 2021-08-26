
def main():
    #Escribe tu código debajo de esta línea
    
  edad= int(input("Ingresa tu edad: "))

if (edad<18):
    print("No cumples requisitos")
elif (edad>=18):
    id= str(input("¿Tienes identificación oficial? (s/n): "))
if (edad>=18) and (id!="s") and (id!="n"):
    print("Respuesta incorrecta")
elif (edad>=18) and (id=="n"):
    print("No cumples requisitos")
elif (edad>=18) and (id=="s"):
    print("Trámite de licencia concedido")
    
    pass


if __name__ == '__main__':
    main()
