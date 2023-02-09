import pandas as pd

# Usamos panda para leer el .xlsx
df = pd.read_excel("recetas.xlsx")

# Leer el archivo de ingredientes
with open("tusingredientes.txt", "r") as file:
    ingredientes = file.read()

# Convertimos todas las filas de la columna ingredientes a str por posibles fallos float
df = df[df['Ingredientes'].apply(lambda x: isinstance(x, str))]

# tokenizamos con .split para el procesamiento.
df['Ingredientes'] = df['Ingredientes'].apply(lambda x: x.split(','))

# el siguiente bucle es el encargado de sacar las recetas parecidas dependiendo del numero de ingredientes que quieres igualar
exit = False
while not exit:

    # Preparamos variables para el bucle que pedira continuamente cuantos ingredientes iguales quieres para comparar las recetas.
    receta_encontrada = False
    num = input("Introduce cuantos ingredientes iguales quieres que tenga la receta: <<para salir introduzca el siguiente codigo: 92541>> : ")
    numint = int(num)
    
    print("_______________RECETAS PARECIDAS_______________")

    # Bucle que compara palabra a palabra fila por fila si son iguales a la lista de ingredientes de la transcripcion
    for index, row in df.iterrows():

        # hacemos un set para evitar palabras iguales
        words = set(row["Ingredientes"])
        # comparamos palabra a palabra
        matching_words = [word for word in words if word in ingredientes]
        # sacamos el numero de palabras iguales 
        matches = len(matching_words)

        # si el numero pasado y la fila tiene el mismo numero de ingredientes, entonces pasa el nombre, el link y finalmente los ingredientes
        if matches == numint:
            receta_encontrada = True
            print(f"Nombre de la receta: {row['Nombre']}")
            print(f"Link de la receta: {row['Link_receta']}")
            print("Ingredientes iguales: ", matching_words) 

    # Si el numero pasado no es igual a palabras iguales entonces dice que no hay ingredientes iguales
    # Si se pasa un codigo especifico cierra el programa
    if not receta_encontrada:
        if numint == 92541:
            print("Saliendo del programa....")
            exit = True
        else:
            print("no hay ninguna receta con ese numero de ingredientes iguales a la receta")
    