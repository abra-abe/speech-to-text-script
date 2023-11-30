import speech_recognition as sr

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=20)

        print('start talking...')

        audio = r.listen(source)

        try:
            print(r.recognize_google(audio, language='en-EN'))

        except Exception as e:
            print('error' + str(e))

        with open("recorded_speech.docx", "w") as f:
            f.write(r.recognize_google(audio, language='en-EN'))

if __name__ == "__main__":
    main()