import speech_recognition as sr

def process_audio(system_language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    try:
        output = r.recognize_google(audio, language=system_language)
    except sr.UnknownValueError:
        output = 1
    except sr.RequestError as e:
        output = 0
    return output