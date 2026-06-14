Gestión de Datos de Países en Python

Trabajo Práctico Integrador - Programación I

Descripción

Este proyecto consiste en un programa de consola desarrollada en Python que permite gestionar información sobre distintos 
países mediante el uso de listas, diccionarios y archivos CSV.

El programa posibilita realizar operaciones de carga, búsqueda, actualización, filtrado, ordenamiento y generación de 
estadísticas, manteniendo la información almacenada en un archivo CSV para conservar los datos entre ejecuciones.

Objetivos del proyecto:
  Aplicar listas y diccionarios.
  Trabajar con funciones y modularización.
  Utilizar archivos CSV para persistencia de datos.
  Implementar validaciones y manejo básico de errores.
  Aplicar técnicas de búsqueda, filtrado, ordenamiento y estadísticas.

Tecnologías utilizadas:
  Python 3.14.0
  Módulo csv
  Listas
  Diccionarios
  Funciones
  Estructuras condicionales y repetitivas
  Manejo de excepciones
  Archivos CSV

Funcionalidades implementadas
1. Agregar país
  Permite registrar un nuevo país indicando:
    Nombre.
    Población.
    Superficie.
    Continente.
   
  Validaciones:
    No se permiten nombres vacíos.
    El nombre no puede contener números.
    La población debe ser mayor que cero.
    La superficie debe ser mayor que cero.
    Solo se aceptan continentes válidos:
      América
      África
      Asia
      Europa
      Oceanía
    No se permiten países duplicados.

2. Actualizar datos
  Permite modificar:
    Población.
    Superficie.
  de un país ya existente.

  Validaciones:
    El país debe existir.
    Los nuevos valores deben ser números enteros positivos.

3. Buscar país
  Permite consultar la información de un país específico mostrando:
    Nombre.
    Población.
    Superficie.
    Continente.

4. Filtrar países
  Se pueden realizar filtros por:
    Continente
    Muestra todos los países pertenecientes a un continente determinado.
  Rango de población
    Permite mostrar los países cuya población se encuentre entre un valor mínimo y máximo.
  Rango de superficie
    Permite mostrar los países cuya superficie se encuentre dentro de un intervalo determinado.

5. Ordenar países
  Los registros pueden ordenarse por:
    Nombre.
    Población.
    Superficie.
  Además, el usuario puede elegir:
    Orden ascendente.
    Orden descendente.
  Para realizar los ordenamientos se utiliza la función sorted() junto con expresiones lambda.

6. Estadísticas
  El sistema calcula automáticamente:
    País con mayor población.
    País con menor población.
    Promedio de población.
    Promedio de superficie.
    Cantidad de países por continente.

Manejo de errores
  El programa incorpora:
    Excepciones personalizadas:
    DatoInvalido
    DatoDuplicado
    Captura de errores mediante:
      try
      except

para evitar fallos por:
  Datos inválidos.
  Valores numéricos incorrectos.
  Archivos inexistentes.
  Países duplicados.
  Consultas sin resultados.

Menú principal
  1. Agregar país
  2. Actualizar datos de población y superficie
  3. Buscar país
  4. Filtrar países
  5. Ordenar países
  6. Mostrar estadísticas
  7. Salir

Integrantes
  Integrante 1: Ariel Bnejamin Cattani
  Integrante 2: Bautista Hidalgo
