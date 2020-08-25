from music21 import *
from cadences import *
import os
import subprocess, shlex
import random
import sys


### Helper Function to isolate final notes of midi Chunk into music theoretic chord


def grabFinalNotes(lastBar):
    finalNotes = []
    allNotes = []
    for mus in lastBar.flat.notes:
        print(mus)
        allNotes.append(mus)
        if (mus.duration.quarterLength + mus.offset) >= 4.0:
            finalNotes.append(mus)
    resList = list(filter(lambda x: type(x) == chord.Chord, finalNotes))
    allList = list(filter(lambda x: type(x) == chord.Chord, allNotes))
    if len(resList) != 0:
        return resList[0]
    return chord.Chord(allNotes[0])



### Globals


'''
Change These Variables to the following:
bundle_path - where your copy of the bundled model is saved
newChunkBasePath - where you want the midi chunks to be stored during creation
outMidiPath - where you want the midi chunks to be stored once the program is finished
exe - your path to polyphony_RNN_generate is
'''

bundle_path = '/Users/znovack/Desktop/Networks/7700_PolyRNN_Impress/polyphony_rnn.mag'


newChunkBasePath = "/Users/znovack/Desktop/Networks/7700_PolyRNN_Impress/generated/"

outMidiPath = "/Users/znovack/Desktop/Networks/7700_PolyRNN_Impress/outMidiFiles"

exe = '/Library/Frameworks/Python.framework/Versions/3.7/bin/polyphony_RNN_generate'

'''
These shouldn't need to be changed
'''

initString = f'--config=polyphony_rnn --bundle_file={bundle_path} --hparams="batch_size=128,rnn_layer_sizes=[256,256,256]" --output_dir={newChunkBasePath} --num_outputs=1 --num_steps=64 --primer_pitches="[45,52,59,66]" --condition_on_primer=true --inject_primer_during_generation=false'

majorCadences = [majorPlagalToMajor, majorPlagalToMinor, majorPerfectToMajor,
                 majorPerfectToMinor, majorBackdoorToMajor, majorBackdoorToMinor]

minorCadences = [minorPlagalToMajor, minorPlagalToMinor, majorPerfectToMajor,
                 minorPerfectToMinor, minorBackdoorToMajor, minorBackdoorToMinor]

neutralCadences = [randomQuartal, randomQuintal, randomHarmonic]



### Main File Creation Function

def makeNewChunk(inFilePath, numBeats):
    mid = converter.parse(inFilePath, format = "midi").chordify()
    midLastBar = mid.measures(4,4)
    
    
    inChord = grabFinalNotes(midLastBar)
    
    if inChord.quality == "major":
        outStr = majorCadences[random.randint(0, len(majorCadences)-1)](inChord)
    elif inChord.quality == "minor":
        outStr = minorCadences[random.randint(0, len(minorCadences)-1)](inChord)
    else:
        outStr = neutralCadences[random.randint(0, len(neutralCadences)-1)](inChord)
    
    argString = '--config=polyphony_rnn --bundle_file=' + bundle_path + ' --hparams="batch_size=128,rnn_layer_sizes=[256,256,256]" --output_dir=' + newChunkBasePath + ' --num_outputs=1 --num_steps=' + str(numBeats*4) + ' --primer_pitches="'+ outStr + '" --condition_on_primer=true --inject_primer_during_generation=false'
    args = shlex.split(argString)
    subprocess.run(args, executable = exe)




### Main function

def main():
    assert(len(sys.argv) == 2)
    num = int(sys.argv[1])
    assert(num >= 1)
    init = shlex.split(initString)
    subprocess.run(init, executable = exe)
    inFile = str(subprocess.run(["ls", newChunkBasePath],
    capture_output = True).stdout)[2:25]
    inFilePath = newChunkBasePath + inFile
    for i in range(num - 1):
        if i != num - 1:
            makeNewChunk(inFilePath, 16)
        else:
            makeNewChunk(inFilePath, 2)
        subprocess.run(["mv", inFilePath, outMidiPath])
        newChunk = str(subprocess.run(["ls", newChunkBasePath],
        capture_output = True).stdout)[2:25]
        newChunkPath = newChunkBasePath + newChunk
        inFilePath = newChunkPath
    subprocess.run(["mv", inFilePath, outMidiPath])
    print("SHE'S DONE!!!!!")
    
###
main()
