import view, controller
from music import *

global score = Score() # create empty score

# takes a default score in the root file directory 
# clones it, and the cloned file will be what is manipulated throughout
# returns the new score       
def readNewMIDISong():
   score = Read.midi(score, "song.mid") # read MIDI file into it   
   return score

# Basic addition of parts based on instrument. 
# Only 5 are included as of to serve as the MVP
# Channel restrictions are observed.
def addPart(argument):
   if argument == "Piano":
      part = Part("Piano Part",PIANO,0)
   elif argument == "Guitar":
      part = Part("Guitar Part", GUITAR, 1)
   elif argument == "Bass":
      part = Part("Bass Part", GUITAR, 2)
   elif argument == "Gunshot":
      part = Part("Gun Part", GUNSHOT, 3)
   elif argument == "Drums":
      part = Part("Percussion Part", STEEL_DRUMS, 9)

   return part

# used to view component parts of the working score
def viewParts():
   return score.getPartList()

# used to view component phrases within a specified part
def viewPhrases(part):
   return part.getPhraseList()

# used to loop a particular phrase
def loopPhrase(part,phr,timesToLoop):
   for i in range(timesToLoop)
   part.addPhrase(phr)
   return part

# flips the entire score between major and minor - other musical modes can be added at later stages of development 
def changeQuality(quality):
   if score.getKeyQuality() == 0:
      score.setKeyQualty(1)
   elif score.getKeyQuality() == 1:
      score.setKeyQuality(0)
