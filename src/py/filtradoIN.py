import spacy
import csv

# Este class sirve para hacer un primer filtrado de la transcripcion
class filtradoi():
    
    print("Filtrando 1/2....")
    

    # Con la siguiente funcion cogeriamos el texto de la transcipcion y lo procesariamos utilizando el modelo
    # es_core_news_sm, pone todo en minuscula y elimina stop words. 
    def normalizar(text):
        nlp = spacy.load('es_core_news_sm')
        doc = nlp(text)
        words = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
        lexical_tokens = [t.lower() for t in words if len(t) > 3 and     
        t.isalpha()]
        return lexical_tokens
    
    # abrimos el .csv anteriormente creado con el metodo transcribir()
    with open('transcription.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            text = ' '.join(row)
        
    # utilizamos la funcion normalizar
    word_list = normalizar(text)

    # Finalmente introducimos las palabras a un .txt
    fich = open('transcripcionF1.txt', "w")
    fich.write('\n'.join(word_list))
    fich.close()
    