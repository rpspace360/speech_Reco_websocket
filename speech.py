import speech_recognition as sr
import asyncio
import datetime
import random
import websockets



async def time(websocket, path):
    
    r = sr.Recognizer()
    m = sr.Microphone()
    while True:
        text = ""
        print("Say somethig!")
        with m as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            r.pause_threshold = 0.6
            r.operation_timeout = 6
            audio = r.listen(source=source, timeout=5)
            print("Got it! Now to recognize it...")

            # try:
            #     print("Sphinx thinks you said " + r.recognize_sphinx(audio_data=audio, keyword_entries=[('next',0.01)]))
            # except sr.UnknownValueError:
            #     print("Sphinx could not understand audio")
            # except sr.RequestError as e:
            #     print("Sphinx error; {0}".format(e))

            try:

                value = r.recognize_google(audio)
                # value = r.recognize_google_cloud(audio_data=audio)
                # value = r.recognize_bing(audio_data=audio, key="933596b75bdd4e418096876d7fa98635", region="westus")
                text = value
                print("You said: {}".format(text))
                

            except sr.UnknownValueError:
                print("Google Speech could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech service; {0}".format(e))
            except sr.WaitTimeoutError as e:
                print("Timeout; {0}".format(e))

            await websocket.send(text)
            

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