import csv

class DatoInvalido(Exception):
    pass
class DatoDuplicado(Exception):
    pass

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
    lista.clear()
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
        print("El archivo al que intenta acceder no se encuentra!")
    return lista

def guardar_paises(nombre_archivo, lista):
    campos = ["nombre", "poblacion", "superficie", "continente"]
    
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        
        escritor.writeheader()
        
        for pais in lista:
            escritor.writerow(pais)

def agregar_pais(nombre_archivo, lista):
        try:
            nombre = input("Ingrese el nombre del país a agregar: ").capitalize()
            
            if nombre.strip() == "":
                raise DatoInvalido("El nombre no puede estar vacío")
                
            duplicado = False
            for pais in lista:
                if nombre == pais["nombre"]:
                    duplicado = True
                    
            if duplicado:
                raise DatoDuplicado("El pais que intenta a gregar ya se encuentra en la planilla")
                
            poblacion = int(input(f"Ingrese la población de {nombre}: "))
            
            if poblacion <= 0:
                raise DatoInvalido("El país no puede estar deshabitado!")
                
            superficie = int(input(f"Ingrese la superficie de {nombre}: "))
            
            if superficie <= 0:
                raise DatoInvalido(f"{nombre} no puede tener una superficie menor o igual a 0!!")
                
            continente = input(f"En cual continente se encuentra {nombre}?: ").capitalize()
            
            if continente != "America" and continente != "Africa" and continente != "Asia" and continente != "Europa" and continente != "Oceania":
                raise DatoInvalido("Su país no puede pertenecer a un continente inexistente!")
            
            pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
            lista.append(pais)
            
            print("País añadido con éxito!")
            guardar_paises(nombre_archivo, lista)
            
        except DatoDuplicado as e:
            print(e)
        except DatoInvalido as e:
            print(e)
        except ValueError:
            print("Lo ingresado debe ser un numero!")

def act_datos(nombre_archivo, lista):
    try:
        nombre = input("Ingrese el nombre del pais que desea cambiar los datos: ").capitalize().strip()
        encontrado = False
        
        if nombre == "":
            raise DatoInvalido("El nombre no puede estar vacío!")
        
        while True:
            try:
                for pais in lista:
                    if nombre == pais["nombre"]:
                        encontrado = True
                        print(f"Poblacion actual de {nombre}: {pais["poblacion"]}")
                        poblacion_act = int(input(f"Cual será la nueva población de {nombre}?: "))
                        
                        if poblacion_act <= 0:
                            raise DatoInvalido("La nueva población no puede ser 0 o menor!")
                            
                        print(f"Superficie actual de {nombre}: {pais["superficie"]}")
                        superficie_act = int(input(f"Cual es la nueva superficie de {nombre}?: "))
                        
                        if superficie_act <= 0:
                            raise DatoInvalido("La superficie no puede ser 0 o menor!")
                            
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
                print("El dato ingrsado deben ser solo numeros")
                
    except DatoInvalido as e:
        print(e)


def buscar_pais(lista):
    consulta = input("Inserte el país que quiera buscar: ").capitalize()
    encontrado = False
    
    for pais in lista:
        if consulta == pais["nombre"]:
            print(f"País: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True
            
    if not encontrado:
        print("El país ingresado no se encuentra en la lista de países")

def filtrar_paises(lista):
    pass