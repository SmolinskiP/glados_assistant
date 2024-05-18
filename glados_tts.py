import torch
from utils.tools import prepare_text
from scipy.io.wavfile import write
import time
from sys import modules as mod
try:
    import winsound
except ImportError:
    from subprocess import call
from os import listdir

from phonemizer.backend.espeak.wrapper import EspeakWrapper
EspeakWrapper.set_library('C:\Program Files\eSpeak NG\libespeak-ng.dll')


# Select the device
if torch.is_vulkan_available():
    device = 'vulkan'
if torch.cuda.is_available():
    device = 'cuda'
else:
    device = 'cpu'

# Load models
glados = torch.jit.load('models/glados.pt')
vocoder = torch.jit.load('models/vocoder-gpu.pt', map_location=device)

# Prepare models in RAM
for i in range(4):
    init = glados.generate_jit(prepare_text(str(i)))
    init_mel = init['mel_post'].to(device)
    init_vo = vocoder(init_mel)

def prepare_audio(input_list):
    for item in input_list:
        tts_glados(item, cache=True)

def tts_glados(input_text, cache=False):
    text = input_text
    if cache == True:
        filename = text.replace(" ", "")
        filename = filename.replace(",", "")
        filename = filename.replace("?", "")
        filename = filename.replace(".", "")
        filename = filename.replace("'", "")
        filename += ".wav"
        cached_files = listdir("voice")
        if filename in cached_files:
            filename = "voice\\" + filename
            if 'winsound' in mod:
                winsound.PlaySound(filename, winsound.SND_FILENAME)
            else:
                call(["aplay", filename])
        else:
            x = prepare_text(text).to('cpu')
            with torch.no_grad():
                tts_output = glados.generate_jit(x)
                mel = tts_output['mel_post'].to(device)
                audio = vocoder(mel)
                audio = audio.squeeze()
                audio = audio * 32768.0
                audio = audio.cpu().numpy().astype('int16')
                output_file = ('voice\\' + filename)
                write(output_file, 22050, audio)

                if 'winsound' in mod:
                    winsound.PlaySound(output_file, winsound.SND_FILENAME)
                else:
                    call(["aplay", output_file])
    else:
        x = prepare_text(text).to('cpu')
        with torch.no_grad():
            tts_output = glados.generate_jit(x)
            mel = tts_output['mel_post'].to(device)
            audio = vocoder(mel)
            audio = audio.squeeze()
            audio = audio * 32768.0
            audio = audio.cpu().numpy().astype('int16')
            output_file = ('voice\\output.wav')
            write(output_file, 22050, audio)

            if 'winsound' in mod:
                winsound.PlaySound(output_file, winsound.SND_FILENAME)
            else:
                call(["aplay", output_file])

def tts_glados_prod(input_text, cache=False):
    text = input_text
    if cache == True:
        filename = text.replace(" ", "")
        filename = filename.replace(",", "")
        filename = filename.replace("?", "")
        filename = filename.replace(".", "")
        filename = filename.replace("'", "")
        filename += ".wav"
        cached_files = listdir("voice")
        if filename in cached_files:
            filename = "voice\\" + filename
            if 'winsound' in mod:
                winsound.PlaySound(filename, winsound.SND_FILENAME)
            else:
                call(["aplay", filename])
        else:
            if 'winsound' in mod:
                winsound.PlaySound("voice\\IdontunderstandwhatyousaidEithermyvoicerecognitioncoregotcorruptedoryouareamoronPropablythesecondone.wav", winsound.SND_FILENAME)
            else:
                call(["aplay", "voice\\IdontunderstandwhatyousaidEithermyvoicerecognitioncoregotcorruptedoryouareamoronPropablythesecondone.wav"])
    else:
        if 'winsound' in mod:
            winsound.PlaySound("voice\\IdontunderstandwhatyousaidEithermyvoicerecognitioncoregotcorruptedoryouareamoronPropablythesecondone.wav", winsound.SND_FILENAME)
        else:
            call(["aplay", "voice\\IdontunderstandwhatyousaidEithermyvoicerecognitioncoregotcorruptedoryouareamoronPropablythesecondone.wav"])