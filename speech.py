import speech_recognition as sr
import asyncio
import datetime
import random
import websockets

text = ""


async def time(websocket, path):
    r = sr.Recognizer()
    m = sr.Microphone()
    while True:
        print("Say somethig!")
        with m as source:
            r.adjust_for_ambient_noise(source, duration=3) 
            r.pause_threshold = 0.5
            audio = r.listen(source)
            print("Got it! Now to recognize it...")

            # try:
            #     print("Sphinx thinks you said " + r.recognize_sphinx(audio_data=audio, keyword_entries=[('next',0.01)]))
            # except sr.UnknownValueError:
            #     print("Sphinx could not understand audio")
            # except sr.RequestError as e:
            #     print("Sphinx error; {0}".format(e))

            try:

                value = r.recognize_google(audio)
                text = value
                print("You said: {}".format(text))
                await websocket.send(text)
                await asyncio.sleep(3)

            except sr.UnknownValueError:
                print("Oops")
            now = datetime.datetime.utcnow().isoformat() + "Z"
            

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


# def Voice():

#     r = sr.Recognizer()
#     m = sr.Microphone()



#     while True:
#         print("Say somethig!")
#         with m as source:
#             r.adjust_for_ambient_noise(source, duration=3) 
#             r.pause_threshold = 0.5
#             audio = r.listen(source)
#             print("Got it! Now to recognize it...")

#             # try:
#             #     print("Sphinx thinks you said " + r.recognize_sphinx(audio_data=audio, keyword_entries=[('next',0.01)]))
#             # except sr.UnknownValueError:
#             #     print("Sphinx could not understand audio")
#             # except sr.RequestError as e:
#             #     print("Sphinx error; {0}".format(e))

#             try:

#                 value = r.recognize_google(audio)
#                 text = value
#                 print("You said: {}".format(text))

#             except sr.UnknownValueError:
#                 print("Oops")

# Voice()