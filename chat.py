import google.generativeai as genai
import os

# Configura tu clave de API de Google Gemini (reemplaza 'TU_CLAVE_API' con tu clave real)
genai.configure(api_key=os.getenv(""))

# Define el modelo a utilizar (puedes cambiarlo según tus necesidades)
MODELO = "gemini-pro"

def iniciar_chat():
    """Inicia una conversación de chat."""
    
    modelo = genai.GenerativeModel(MODELO)
    chat = modelo.start_chat()

    print("¡Hola! Puedes comenzar a chatear (escribe 'salir' para terminar).")

    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == "salir":
            print("¡Hasta luego!")
            break

        respuesta = chat.send_message(pregunta)
        print("Gemini:", respuesta.text)

if __name__ == "__main__":
    iniciar_chat()