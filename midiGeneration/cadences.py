from music21 import *

### Universal Helper Functions
def addBass(inChord, root):
    lowNote = inChord.bass()
    while(lowNote.midi <= root.midi):
        root = pitch.Pitch(root.midi-12)
    octaveHigh = root
    fifth = pitch.Pitch(root.midi - 5)
    octaveLow = pitch.Pitch(root.midi - 12)
    for note in [octaveHigh, fifth, octaveLow]:
        if note.octave != None:
            inChord.add(note)
    return inChord


def getOutChord(inDegs, outDegs):
    for deg in inDegs:
        if (inDegs[deg] == None or outDegs[deg] == None) and len(outDegs) > 1:
            del outDegs[deg]
            print(outDegs)
    res = list(outDegs.values())
    while None in res:
        res.remove(None);
    if len(res) == 0:
        return list(inDegs.values())
    return res


def makeMidiString(outChord):
    outMidi = []
    print(outChord)
    print(outChord.pitchedCommonName)
    for n in outChord.pitches:
        outMidi.append(n.midi)
    outStr = "["
    for mid in outMidi:
        outStr += str(mid)
        outStr += ","
    outStr = outStr[0:-1]
    outStr += "]"
    return outStr


### Main Cadential Function

def minorPlagalToMinor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.root().midi-2)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.third.midi-1)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.fifth)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.third.midi+2)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-5))
    
    return makeMidiString(outChord)
    
def minorPlagalToMajor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.root().midi-1)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.third.midi-1)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.fifth)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.third.midi+1)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-5))
    
    return makeMidiString(outChord)

def majorPlagalToMinor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.root().midi-2)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.third.midi-2)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.fifth)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.root().midi-10)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-5))
    
    return makeMidiString(outChord)

def majorPlagalToMajor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.root().midi-1)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.third.midi-2)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.fifth)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.root().midi-10)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-5))
    
    return makeMidiString(outChord)


def randomQuintal(inChord):
    outRoot = pitch.Pitch(inChord.bass().midi-2)
    outFifth = pitch.Pitch(outRoot.midi+7)
    outNinth = pitch.Pitch(outFifth.midi+7)
    outSixth = pitch.Pitch(outNinth.midi+7)
    outThird = pitch.Pitch(outSixth.midi+7)
    outChord = chord.Chord([outRoot, outFifth, outNinth, outSixth, outThird])
    outChord = addBass(outChord, outRoot)
    
    return makeMidiString(outChord)

def randomQuartal(inChord):
    outRoot = pitch.Pitch(inChord.bass().midi-2)
    outFourth = pitch.Pitch(outRoot.midi+5)
    outSeventh = pitch.Pitch(outFourth.midi+5)
    outMin3 = pitch.Pitch(outSeventh.midi+5)
    outMin6 = pitch.Pitch(outMin3.midi+5)
    outChord = chord.Chord([outRoot, outFourth, outSeventh, outMin3, outMin6])
    outChord = addBass(outChord, outRoot)
    
    return makeMidiString(outChord)

def randomHarmonic(inChord):
    outRoot = pitch.Pitch(inChord.bass().midi-5)
    outOct1 = pitch.Pitch(outRoot.midi+12)
    outFifth = pitch.Pitch(outOct1.midi+7)
    outOct2 = pitch.Pitch(outFifth.midi+5)
    outThird = pitch.Pitch(outOct2.midi+4)
    outSeventh = pitch.Pitch(outThird.midi+6)
    outChord = chord.Chord([outRoot, outOct1, outFifth, outOct2, outThird, outSeventh])
    outChord = addBass(outChord, outRoot)
    
    return makeMidiString(outChord)


def majorPerfectToMajor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        if (inChord.seventh != None):
            outThird = pitch.Pitch(inChord.seventh.midi-1)
        else:
            outThird = pitch.Pitch(inChord.root().midi-3)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.root().midi)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.third+1)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.third.midi-2)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-7))
    
    return makeMidiString(outChord)


def majorPerfectToMinor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        if (inChord.seventh != None):
            outThird = pitch.Pitch(inChord.seventh.midi-2)
        else:
            outThird = pitch.Pitch(inChord.root().midi-4)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.root().midi)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.third+1)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.third.midi-1)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-7))
    
    return makeMidiString(outChord)


def minorPerfectToMajor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        if (inChord.seventh != None):
            outThird = pitch.Pitch(inChord.seventh.midi-1)
        else:
            outThird = pitch.Pitch(inChord.root().midi-3)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.root().midi)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.third+2)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.third.midi-1)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-7))
    
    return makeMidiString(outChord)


def minorPerfectToMinor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        if (inChord.seventh != None):
            outThird = pitch.Pitch(inChord.seventh.midi-2)
        else:
            outThird = pitch.Pitch(inChord.root().midi-4)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.root().midi)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.third+2)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.third.midi)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-7))
    
    return makeMidiString(outChord)


def majorBackdoorToMajor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.third.midi+2)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.fifth.midi+2)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.root()+2)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.root()+13)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-10))
    
    return makeMidiString(outChord)

def majorBackdoorToMinor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.third.midi+1)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.fifth.midi+2)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.root()+2)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.root()+12)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-10))
    
    return makeMidiString(outChord)

def minorBackdoorToMajor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.fifth.midi-1)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.fifth.midi+2)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.root()+2)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.root()+13)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-10))
    
    return makeMidiString(outChord)

def minorBackdoorToMinor(inChord):
    outRoot = outThird = outFifth = outSeventh = None
    try:
        outThird = pitch.Pitch(inChord.third.midi+2)
    except:
        print("no 3rd")
    try:
        outFifth = pitch.Pitch(inChord.fifth.midi+2)
    except:
        print("no 5th")
    try:
        outRoot = pitch.Pitch(inChord.root()+2)
    except:
        print("no root")
    try:
        outSeventh = pitch.Pitch(inChord.root()+12)
    except:
        print("no 7th")
    
    inDegs = {3:inChord.root(), 5: inChord.third,
                1: inChord.fifth, 7: inChord.seventh}
    
    outChordDict = {1:outRoot, 3:outThird, 5:outFifth, 7:outSeventh}
    
    
    outChordList = getOutChord(inDegs, outChordDict)
    outChord = chord.Chord(outChordList)
    outChord = addBass(outChord, pitch.Pitch(inChord.root().midi-10))
    
    return makeMidiString(outChord)