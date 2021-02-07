import fluidsynth
import os

fs = fluidsynth.Synth()
fs.start()

def getSoundfonts():
    soundfonts = []
    for file in os.listdir("/usr/local/share/soundfonts"):
        if file.endswith(".sf2") or file.endswith(".sf3"):
            soundfonts.append(file)
    if soundfonts:
        return soundfonts
    else:
        return "No soundfonts detected!"

def getPatches(soundfont):
    try:
        sfid = fs.sfload(soundfont)

    except:
        return "No patches in soundfont!"
