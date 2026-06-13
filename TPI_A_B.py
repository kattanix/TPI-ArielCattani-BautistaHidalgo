from fcs_A_B import *
import csv 

paises = []

limpiar_pantalla()

cargar_paises("paises.csv", paises)

while True:


    menu()
    
    opcion = input("\n» Opción: ")
    
    
    match opcion:
        case "1":
            agregar_pais("paises.csv", paises)
        case "2":
            act_datos("paises.csv", paises)
        case "3":
            buscar_pais(paises)
        case "4":
            filtrar_paises(paises)
        case "5":
            ordenar_paises(paises)
        case "6":
            mostrar_estadisticas(paises)
        case "7":
            limpiar_pantalla()
            print("Cerrando programa...")
            break
        
        case "-":
            print(paises)
            
        case _ :
            limpiar_pantalla()
            print("! Opcion no valida - Seleccione las opciones que se encuentran en pantalla")
            