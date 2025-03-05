nombreVendedor=None
productos=[]
producto={}

opcion=100

print("Mercado")
print("1. Crear lista de mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista ")
print("4. Retirar pproductos de lista ")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opcion: "))

    if opcion == 1:
        print ("Bienvenido a la creacion de tu lista de mercado")
        #creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]= input("digite el nombre del producto:")
        producto["precio"]=int(input("Digite el precio del producto:"))
        producto["cantidad"]=int(input("cuantas unidades vas a llevar: "))
        producto["presentacion"]=input("en que presentacion lo deseas ")


        #provar el diccionario
       # print(producto)

        #poblar elementos a una lista 

        productos.append(producto)
        print(productos)

    elif opcion == 2:
        print ("estoy en la dos")
    elif opcion == 3:
        print (" estoy en la tres")
    elif opcion == 4:
        print("estoy en la cuatro")
    else:
        print("opcion invalida")        