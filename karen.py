import speech_recognition as sr
import pyttsx3
import ollama
from app import APPLICATIONS

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

    elif "heure" in commande:
        from datetime import datetime
        heure = datetime.now().strftime("%H heures %M")
        parler("Il est : " + heure)

    elif "date" in commande or "jour" in datetime:
        from datetime import datetime
        jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
        mois = ["janvier", "février", "mars", "avril", "mai", "juin",
                "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

        maintenant = datetime.now()
        jour = jours[maintenant.weekday()]
        date = str(maintenant.day) + " " + mois[maintenant.month - 1] + " " + str(maintenant.year)
        parler("Nous sommes " + jour + " " + date)

    #ouverture d'application
    elif "ouvre" in commande :
        import os
        app_trouvee = False
        for nom, chemins in APPLICATIONS.items():
            if nom in commande:
                os.startfile(chemins)
                parler("J'ouvre " + nom)
                app_trouvee = True
                break
            if not app_trouvee:
                parler("Je ne trouve pas cette application.")
    else:
        response = reflechir(commande)
        parler(response)