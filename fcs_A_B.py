import csv

class DatoInvalido(Exception):
    pass
class DatoDuplicado(Exception):
    pass



import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print("""
1. Agregar país.
2. Actualizar datos de población y superficie.
3. Buscar país
4. Filtrar paises
5. Ordenar paises
6. Mostrar estadisticas
7. Salir""")


def cargar_paises(nombre_archivo, lista):
    
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                
                lista.append(pais)
    except FileNotFoundError:
        limpiar_pantalla()
        print("! El archivo al que intenta acceder no se encuentra")
    return lista




def guardar_paises(nombre_archivo, lista):
    campos = ["nombre", "poblacion", "superficie", "continente"]
    
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        
        escritor.writeheader()
        
        for pais in lista:
            escritor.writerow(pais)



def agregar_pais(nombre_archivo, lista):
    
    
    continentes_validos = [
    "America",
    "Africa",
    "Asia",
    "Europa",
    "Oceania"
]

    limpiar_pantalla()
    
    try:
            nombre = input("Ingrese el nombre del país a agregar: ").capitalize()
            
            if nombre.strip() == "":
                raise DatoInvalido("El nombre no puede estar vacío")
                
            duplicado = False
            for pais in lista:
                if nombre == pais["nombre"]:
                    duplicado = True
                    
            if duplicado:
                raise DatoDuplicado("! El pais que intenta agregar ya se encuentra en la planilla")
            
            limpiar_pantalla()
            
            
            print(f"- Nombre: {nombre}")
            poblacion = int(input(f"Ingrese la población de {nombre}: "))
            
            if poblacion <= 0:
                raise DatoInvalido("! El país no puede estar deshabitado")
            
            limpiar_pantalla()
            print(f"- Nombre: {nombre}")
            print(f"- Poblacion: {poblacion}")
            
            superficie = int(input(f"Ingrese la superficie de {nombre}: "))
            
            if superficie <= 0:
                raise DatoInvalido(f"! {nombre} no puede tener una superficie menor o igual a 0")
            
            limpiar_pantalla()
            print(f"- Nombre: {nombre}")
            print(f"- Población: {poblacion}")
            print(f"- Superficie: {superficie}")
            
            continente = input(f"? En que continente se encuentra {nombre}: ").capitalize()
            
            
            
            if continente not in continentes_validos:
                raise DatoInvalido("! Su país no puede pertenecer a un continente inexistente")
            
            
            pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
            lista.append(pais)
            
            limpiar_pantalla()
            print(f"- Nombre: {nombre}")
            print(f"- Población: {poblacion}")
            print(f"- Superficie: {superficie}")
            print(f"- Continente: {continente}")
            
            print("¡País añadido con éxito!")
            guardar_paises(nombre_archivo, lista)
            
    except DatoDuplicado as e:
            print(e)
    except DatoInvalido as e:
            print(e)
    except ValueError:
            print("! Lo ingresado debe ser un numero")








def act_datos(nombre_archivo, lista):
    
    limpiar_pantalla()
    
    try:
        nombre = input("Ingrese el nombre del pais que desea cambiar los datos: ").capitalize().strip()
        encontrado = False
        
        if nombre == "":
            limpiar_pantalla()
            raise DatoInvalido("! El nombre no puede estar vacío")
        
        while True:
            print(f"Actualizando datos de {nombre}...\n")
            
            try:
                for pais in lista:
                    if nombre == pais["nombre"]:
                        encontrado = True
                        
                        print(f"- Poblacion actual de {nombre}: {pais['poblacion']}")
                        
                        poblacion_act = int(input(f"? Cual será la nueva población de {nombre}: "))
                        
                        if poblacion_act <= 0:
                            raise DatoInvalido("! La nueva población no puede ser 0 o menor")
                            
                        print(f"- Superficie actual de {nombre}: {pais['superficie']}")
                        superficie_act = int(input(f"? Cual es la nueva superficie de {nombre}: "))
                        
                        if superficie_act <= 0:
                            raise DatoInvalido("! La superficie no puede ser 0 o menor")
                            
                        pais["poblacion"] = poblacion_act
                        pais["superficie"] = superficie_act
                        
                        print("Datos cambiados con éxito!")
                        guardar_paises(nombre_archivo, lista)
                        return
                        
                if not encontrado:
                    print("El país ingresado no se encuentra en la lista de países")
                    break
                    
            except DatoInvalido as e:
                print(e)
            except ValueError:
                limpiar_pantalla()
                print(f"Actualizando datos de {nombre}...")
                print("! El dato ingresado deben ser solo numeros")
                
    except DatoInvalido as e:
        print(e)


def buscar_pais(lista):
    limpiar_pantalla()
    
    print("\n-: Busqueda de países :-\n")
    consulta = input("Inserte el país que quiera buscar: ")
    encontrado = False
    
    
    for pais in lista:
        if consulta.lower().strip() == pais["nombre"].lower().strip():
            print(f"- País: {pais['nombre']}")
            print(f"- Población: {pais['poblacion']}")
            print(f"- Superficie: {pais['superficie']}")
            print(f"- Continente: {pais['continente']}")
            encontrado = True
            
    if not encontrado:
        print("El país ingresado no se encuentra en la lista de países")





def filtrar_paises(lista):

    limpiar_pantalla()
    while True:
        
        print("""
    1. Filtrar por continente
    2. Filtrar por población
    3. Filtrar por superficie
    4. « Volver 
    """)

        opcion = input("Seleccione filtro: ")
        
        match opcion:
            
                case "1":
                    limpiar_pantalla()
                    continente = input("Ingrese continente: ")
                    
                    encontrados = False
                    
                    limpiar_pantalla()
                    
                    print(f"- Países de {continente.capitalize()}")
                    print()
                    for pais in lista:
                        
                        if pais["continente"].lower().strip() == continente.lower().strip():
                            print("-"*20)
                            print(f"- Pais: {pais['nombre']}")
                            print(f"- Poblacion: {pais['poblacion']}")
                            print(f"- Superficie: {pais['superficie']}")
                            print(f"- Continente: {pais['continente']}")
                            
                            
                            encontrados = True
                            
                    if not encontrados:
                        limpiar_pantalla()
                        print("! No se encontraron países.")
                
                
                case "2":
                    limpiar_pantalla()
                    while True:
                        try:
                            
                            minimo = int(input("Poblacion minima: "))
                            
                            if minimo < 0:
                                limpiar_pantalla()
                                print("Error: No puede ser menor a 0")
                                continue
                            
                            break
                        
                        except ValueError:
                            limpiar_pantalla()
                            print("Error: Debe ingresar solo numeros enteros")

                    
                    limpiar_pantalla()

                    
                    while True:
                        try:
                            print(f"- Rango minimo: {minimo}")  
                            maximo = int(input("Población maxima: "))
                                
                            if maximo < 0:
                                limpiar_pantalla()
                                print("! Error: No puede ser menor a 0")
                                continue
                            
                            if minimo > maximo:
                                print("! El mínimo no puede ser mayor al máximo")
                                continue
                            
                            break
                        
                        except ValueError:
                            limpiar_pantalla()
                            print("! Error: Debe ingresar solo numeros enteros")


                    
                    encontrado = False
                    
                    print()
                    for pais in lista:
                        
                        if minimo <= pais["poblacion"] <= maximo:
                                print("-"*10, " ··· ", "-"*10)
                                
                                print(f"- Pais: {pais['nombre']}")
                                print(f"- Poblacion: {pais['poblacion']}")
                                print(f"- Superficie: {pais['superficie']}")
                                print(f"- Continente: {pais['continente']}")
                            
                                
                                encontrado = True
                    print()
                    
                    if not encontrado:
                        limpiar_pantalla()
                        print("No se encontraron países con ese rango de población")
                     


    
                case "3":
                    
                    limpiar_pantalla()
                    while True:
                        print("-: Filtrar por población :-\n")
                        
                        try:
                            
                            minimo = int(input("Superficie minima: "))
                            
                            if minimo < 0:
                                limpiar_pantalla()
                                print("Error: No puede ser menor a 0")
                                continue
                            break
                        
                        except ValueError:
                            limpiar_pantalla()
                            print("Error: Debe ingresar solo numeros enteros")

                    
                    limpiar_pantalla()

                    
                    while True:
                        print("Filtrar por población\n")
                        
                        try:
                            print(f"- Rango minimo: {minimo}")  
                            maximo = int(input("Superficie maxima: "))
                                
                            if maximo < 0:
                                limpiar_pantalla()
                                print("! Error: No puede ser menor a 0")
                                continue
                            break
                        
                        except ValueError:
                            limpiar_pantalla()
                            print("! Error: Debe ingresar solo numeros enteros")

                    
                    encontrado = False
                    
                    for pais in lista:

                        if minimo <= pais["superficie"] <= maximo:
                            
                            print("-"*20)
                            print(f"- Pais: {pais['nombre']}")
                            print(f"- Poblacion: {pais['poblacion']}")
                            print(f"- Superficie: {pais['superficie']}")
                            print(f"- Continente: {pais['continente']}")
                            
                            encontrado = True
                    
                    print()
                            
                        
                    if not encontrado:
                        limpiar_pantalla()
                        print("ı: No se encontraron paises en ese rango de superficie.")
                                    
                       
                        
                case "4":
                    limpiar_pantalla()
                    break
                
                case _:
                    limpiar_pantalla()
                    print("! No valido - Seleccione las opciones que se encuentran en pantalla")





def ordenar_paises(lista):
    limpiar_pantalla()
    
    
    while True:
        print("""
    1. Nombre
    2. Población
    3. Superficie
    4. « Volver
    """)

        opcion = input("? Ordenar por: ")
        
        if opcion not in ["1", "2", "3", "4"]:
            limpiar_pantalla()
            print("Seleccion no valida - Seleccione las opciones que estan en pantalla")
            continue
        
        if opcion == "4":
            limpiar_pantalla()
            break
        
        while True:
            
            sentido = input("Ascendente(A) o Descendente(D): ").upper()

            if sentido not in ["A", "D"]:
                limpiar_pantalla()
                print("Seleccion no valida - Seleccione las opciones que estan en pantalla")
                continue
            break
        
        
        
        reversa = sentido == "D"

        match opcion:

            case "1":
                ordenados = sorted(lista,
                                key=lambda pais: pais["nombre"],
                                reverse=reversa)

            case "2":
                ordenados = sorted(lista,
                                key=lambda pais: pais["poblacion"],
                                reverse=reversa)

            case "3":
                ordenados = sorted(lista,
                                key=lambda pais: pais["superficie"],
                                reverse=reversa)

            case "4":
                limpiar_pantalla()
                break
            
            case _:
                print("! No valido - Seleccione las opciones que se encuentran en pantalla")
                return

        limpiar_pantalla()
        
        if opcion == "1":
            print(f"-: Ordenado por nombre ({'Ascendente' if sentido == 'A' else 'Descendente'}) :-")
        elif opcion == "2":
            print(f"-: Ordenado por población ({'Ascendente' if sentido == 'A' else 'Descendente'}) :-")
        elif opcion == "3":
            print(f"-: Ordenado por superficie ({'Ascendente' if sentido == 'A' else 'Descendente'}) :-")
        
        for pais in ordenados:
            print("-"*20)
            print(f"País: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")






def mostrar_estadisticas(lista):
    
    limpiar_pantalla()

    mayor = max(lista,
                key=lambda pais: pais["poblacion"])

    menor = min(lista,
                key=lambda pais: pais["poblacion"])

    promedio_poblacion = (
        sum(pais["poblacion"] for pais in lista)
        / len(lista)
    )

    promedio_superficie = (
        sum(pais["superficie"] for pais in lista)
        / len(lista)
    )

    continentes = {}

    for pais in lista:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n-: Estadisticas :-\n")

    print(
        f"Mayor población: "
        f"{mayor['nombre']} ({mayor['poblacion']})"
    )

    print(
        f"Menor población: "
        f"{menor['nombre']} ({menor['poblacion']})"
    )

    print("\n - Promedios")
    
    print(
        f"Promedio población: "
        f"{promedio_poblacion:.2f}"
    )

    print(
        f"Promedio superficie: "
        f"{promedio_superficie:.2f}"
    )

    print("\nPaíses por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")