import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('Search on Youtube(say youtube) : ')
    print('Speak Now')
    audio = r3.listen(source)

    if "youtube" in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = "https://www.youtube.com/result?search_query="
        with sr.Microphone() as source:
            print("Search any video(like if you want to search python just say python): ")
            audio = r2.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:
                print("Error")
            except sr.RequestError as e:
                print("Failed to get results".format(e))
