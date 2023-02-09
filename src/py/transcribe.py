import pytube
import whisper
import pandas as pd

# Este class sirve para coger los videos de youtube y sacarlos a texto.

class transcribir():
    # Introducimos primero desde la terminal una url de youtube
    url = input("Introduce un enlace de youtube sobre la receta a comparar: ")
    print("Transcribiendo.....")
    youtubeUrl = url

    # Usamos pytube para descargar el video y guardarlo en un .mp4
    youtubeVideo = pytube.YouTube(youtubeUrl)
    audio = youtubeVideo.streams.get_audio_only()
    audio.download(filename='video1.mp4')

    # Usamos whisper que es un modelo de OpenAI para transcribir a texto una variedad de entradas
    model = whisper.load_model("small")
    result = model.transcribe('video1.mp4')

    # Entonces guardamos el resultado en un .csv usando pandas para crear una columna llamada text
    df = pd.DataFrame([result], columns= ['text'])
    df.to_csv('transcription.csv', index=False)
    

