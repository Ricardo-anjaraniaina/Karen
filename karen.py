import speech_recognition as sr
import pyttsx3
import ollama

def parler(texte):
    print("Karen : " + texte)
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)
    engine.say(texte)
    engine.runAndWait()
    engine.stop()
    del engine

def ecouter():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source :
        print("Karen écoute...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try: 
            audio = recognizer.listen(source, timeout=5)
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print("tu as dis: "+ texte)
            return texte
        except:
            return ""
        
def reflechir(question):
    print("Karen réfléchit...")
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "roles": "system",
                "content": "Tu es Karen, une assistante personnelle intelligente"
            },
            {
                "roles": "user",
                "content": question

            }
        ]
    )
    return response["message"]["content"]

parler("Bonjour, je suis Karen, votre assistante personnelle. Comment puis-je vous aider ?")

while True:
    commande = ecouter()

    if not commande:
        continue

    if "arrête" in commande or "au revoir" in commande or "stop" in commande :
        parler("au revoir")
        break

    if "date" in commande:
        parler("On est le : ")

    response = reflechir(commande)
    parler(response)