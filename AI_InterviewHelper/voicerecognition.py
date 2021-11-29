import speech_recognition as sr

def voiceReco():
    transcript=""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source, phrase_time_limit=200)
    try: 
        transcript = r.recognize_google(audio, language="en-US")
        print("you said: "+transcript)
    except sr.UnknownValueError:
        transcript = "Could not understand audio" 
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return transcript
