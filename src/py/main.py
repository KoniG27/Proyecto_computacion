
# Programa que sirve tanto para pasar video de youtube como para introducir los ingredientes que tu tienes 
# para sacar recetas parecidas/iguales
# Ejecuta todas las clases una por una intenta ejecutarlas y si hubiese algun error sacaria una excepcion.

print("Quieres sacar recetas parecidas con tus ingredientes o desde un video de youtube?")
text = input("Si quieres tus ingredientes introduce: 'vale', si no presiona enter: ")
try:
    if(text == "vale"):
        palabras = []

        while True:
            palabra = input("Introduce un ingrediente o escribe 'salir' para terminar: ")
            if palabra.lower() == 'salir':
                break
            else:
                palabras.append(palabra)
        
        with open("tusingredientes.txt", "w") as f:
            f.write("\n".join(palabras))
        import Exploracion2    
        Exploracion2
    else:
        from transcribe import transcribir
        transcribir()
        try:
            from filtradoIN import filtradoi
            filtradoi()
        except:
            print("Ha ocurrido un error en el filtrado inicial")  
        try: 
            from filtradofinal import filtradof
            filtradof()
        except:
            print("Ha ocurrido un error en el filtrado final")
        try:
            import Exploracion    
            Exploracion       
        except:
            print("Ha ocurrido un error explorando")

except:
    print("Ha ocurrido un fallo en la transcripcion")   


   