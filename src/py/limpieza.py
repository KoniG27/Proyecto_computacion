
# class utilizado porque el dataset de los ingredientes contenia comas.

class limpcomas():
    # Abrir el archivo
    with open("Ingredientes.txt", "r") as file:
    # Leer el contenido del archivo
        text = file.read()

    # Reemplazar las comas por una cadena vacía
    text = text.replace(",", "")


    # Escribir el contenido modificado en un nuevo archivo
    with open("IngredientesL.txt", "w") as file:
        file.write(text)
