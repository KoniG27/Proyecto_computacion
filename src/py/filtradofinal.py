import time

# En esta clase haremos el filtrado final para sacar finalmente los ingredientes del video, comparandolo con un dataset de 1000 ingredientes

class filtradof():
    print("Flitrando 2/2.....")
    time.sleep(2)

    # Abrimos los archivos a comparar
    with open("IngredientesL.txt") as f1, open("transcripcionF1.txt") as f2:

        # Leer el contenido de ambos archivos
        content1 = f1.read()
        content2 = f2.read()
        # Tokenizar el contenido
        palabars1 = content1.split()
        palabras2 = content2.split()
        
        # Encontrar la intersección de ambas listas
        iguales = set(palabras2) & set(palabars1)

        # Eliminar las repeticiones
        palabrasiguales = list(set(iguales))
    
    # Guardamos los ingredientes en un .txt
    fich = open('ingredientesFinal.txt', "w")
    fich.write('\n'.join(palabrasiguales))
    fich.close()
    
    
