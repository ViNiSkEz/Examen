productos={
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'J187HD': ['Asus', 17, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080TI'],
    'B2211HD': ['HP', 13.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '1235HD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
    'C425HD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 13.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock={
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'J187HD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'YS1230HD': [249990, 0],
}
print("bienvenido al sistema de productos de pybooks")
try:
    while(True):
        print("""
            ╔═════════════════════════════════════════╗
            ║         MENU PRINCIPAL PYBOOKS          ║
            ╠═════════════════════════════════════════╣
            ║ 1. Stock marca.                         ║
            ║ 2. Busqueda por precio.                 ║
            ║ 3. Actualizar precio.                   ║
            ║ 4. Salir.                               ║
            ╚═════════════════════════════════════════╝""")
        seleccion=int(input("Porfavor seleccone una opcion: "))

            
        if seleccion==1:
            marca_buscar = input("Ingrese la marca a buscar: ")
            marca_lower = marca_buscar.lower()
            found_any = False
            
            for modelo, details in productos.items():
                if details[0].lower() == marca_lower:
                    if modelo in stock and stock[modelo][1] > 0:
                        print(f"Modelo: {modelo}, Stock: {stock[modelo][1]}")
                        found_any = True
            
            if not found_any:
                print(f"No se encontraron notebooks de la marca '{marca_buscar}' con stock disponible.")
        
        elif seleccion==2:
            p_min=0
            p_max=0
            valid_input=False
            while not valid_input:
                try:
                    p_min_str=input("Ingrese precio mínimo: ")
                    p_min = int(p_min_str)
                    p_max_str=input("Ingrese precio máximo: ")
                    p_max = int(p_max_str)
                    valid_input = True
                except ValueError:
                    print("¡Debe ingresar valores enteros!")
                    
            modelos_encontrados=[]
            for modelo, details in productos.items():
                if modelo in stock:
                    precio=stock[modelo][0]
                    if p_min <= precio <= p_max and stock[modelo][1] > 0:
                        marca=details[0]
                        modelos_encontrados.append(f"{marca}-{modelo}")
            
            n_outer = 0
            while n_outer < len(modelos_encontrados):
                n_inner = 0
                while n_inner < len(modelos_encontrados) - n_outer - 1:
                    if modelos_encontrados[n_inner] > modelos_encontrados[n_inner+1]:
                        temp = modelos_encontrados[n_inner]
                        modelos_encontrados[n_inner] = modelos_encontrados[n_inner+1]
                        modelos_encontrados[n_inner+1] = temp
                    n_inner += 1
                n_outer += 1
            
            if not modelos_encontrados:
                print("¡No hay notebooks en ese rango de precios.")
            else:
                i = 0
                while i < len(modelos_encontrados):
                    print(modelos_encontrados[i])
                    i += 1
                    
        elif seleccion==3:
            while True:
                modelo_actualizar=input("Ingrese el modelo a actualizar: ")
                precio_nuevo=0
                valid_price_input=False
                while not valid_price_input:
                    try:
                        precio_nuevo_str=input("Ingrese precio nuevo: ")
                        precio_nuevo=int(precio_nuevo_str)
                        valid_price_input=True
                    except ValueError:
                        print("¡Debe ingresar un valor numérico para el precio!")
                        
                if modelo_actualizar in stock:
                    stock[modelo_actualizar][0] = precio_nuevo
                    print("Precio actualizado!")
                else:
                    print("El modelo no existe!!")
                
                respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
                if respuesta != 's':
                    break
                
        elif seleccion==4:
            print("adios")
            break
            
        else:
            print("ingrese una opcion valida")
except ValueError:
    print("no se permiten letras ")
                