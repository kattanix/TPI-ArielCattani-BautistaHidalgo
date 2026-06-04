from fcs_A_B import *
import csv 

paises = []

while True:
    cargar_paises("paises.csv", paises)
    menu()
    opcion = input("Ingrese la opcion a elegir: ")
    
    match opcion:
        case "1":
            agregar_pais("paises.csv", paises)
        case "2":
            act_datos("paises.csv", paises)
        case "3":
            buscar_pais(paises)
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Cerrando programa...")
            break
        case "-":
            print(paises)