# Karen

Une assistante personnelle locale, vocale et intelligente tournant entièrement sur votre machine.

## Fonctionnalités

- Écoute vocale via le microphone
- Reconnaissance vocale en français (Google Speech Recognition)
- Réponses générées par un LLM local via Ollama (llama3.2)
- Synthèse vocale (pyttsx3)
- Commandes intégrées : heure, date, arrêt

## Prérequis

- Python 3.10+ (Python 3.11 de préférence pour compatibilité avec pyaudio)
- [Ollama](https://ollama.com) installé avec le modèle `llama3.2`

```bash
ollama pull llama3.2
```

## Installation

```bash
pip install speechrecognition pyttsx3 ollama pyaudio
```

> Sur Windows, si `pyaudio` échoue : `pip install pipwin && pipwin install pyaudio`

## Utilisation

```bash
python karen.py
```

Karen se lance et attend vos commandes vocales.

## Commandes vocales

| Commande | Action |
|---|---|
| "quelle heure est-il" | Donne l'heure actuelle |
| "quelle date" / "quel jour" | Donne la date du jour |
| "arrête" / "au revoir" / "stop" | Arrête Karen |
| Toute autre phrase | Réponse via le LLM |

## Structure

```
Karen/
├── karen.py   # Point d'entrée principal
└── README.md
```
