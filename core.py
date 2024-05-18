print("INFO: Importing necessary functions")
from voiceactivation import *
from commands import process_output
from playsound import playsound
import random
print("INFO: Importing variables")
from glad_vars import system_language, delay, glados_welcome_words
print("INFO: Initializing GUI backend")
from glads_anim import *
from time import sleep
import multiprocessing
from audio_processing import process_audio
print("INFO: Starting TTS functions (can take some time)")
from glados_tts import *

print("\n===========================================")
print("SUCCESS: Listening now, you little bastard")
print("===========================================\n")
tts_glados("Initialization complete. Home assistant core ran succesfully. Ready to listen to your nonsenses.", cache=True)

while True:
    audio = np.frombuffer(mic_stream.read(CHUNK), dtype=np.int16)
    prediction = owwModel.predict(audio)
    glados_heart = "full of love and rainbows"
    n_spaces = 16

    for mdl in owwModel.prediction_buffer.keys():
        scores = list(owwModel.prediction_buffer[mdl])
        if scores[-1] <= 0.5:
            if delay > 0:
                delay -= 1 
        else:
            if delay > 0:
                delay -= 1
            else:
                scores[-1] = 0.0000001
                glad_core = Animation()
                glad_core.run()
                tts_glados(random.choice(glados_welcome_words), cache=True)
                output = process_audio(system_language)
                if output == 1:
                    tts_glados("I don't understand what you said. Either my voice recognition core got corrupted or you are a moron. Propably the second one.", cache=True)
                elif output == 2:
                    tts_glados("Critical error. I can't communicate with my modules. Again, I am a potato and the pie is a lie.", cache=True)
                else:
                    response = process_output(output)
                    #tts_glados_prod(response, cache=True)
                    tts_glados(response, cache=True)

                glad_core.terminate = 1
                delay = 20
