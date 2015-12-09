import view, controller
from music import *

global score = Score() # create the intial empty working score

# Set the working score to a default score in the root file directory        
def readNewMIDISong():
   score = Read.midi(score, "changes.midi") # read the default MIDI file (changes.midi) to working score  
   return score

# Basic addition of parts based on instrument. 
# Only 5 are included as of to serve as the MVP
# Channel restrictions are observed.

def addPianoPart():                       
   part = Part("Piano Part 1",PIANO,0)
   score.addPart(part)

def addGuitarPart():
   part = Part("Guitar Part 1", GUITAR, 1)
   score.addPart(part)

def addBassPart():
   part = Part("Bass Part 1", BASS, 2)
   score.addPart(part)

def addPercussion():
   part = Part("Percussion Part",STEEL_DRUMS, 9)
   score.addPart(part)

def needMoreGunshots():  # breaking naming convention because gunshots don't play by the rules.
   part = Part("All I wanna do is *shot shot* and take your money", GUNSHOT, 16)
   score.addPart(part)
   

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

def movePhraseToOtherPart(phr):
   for i in range(phr):
      
# flips the entire score between major and minor - other musical modes can be added at later stages of development 
def changeQuality(quality):
   if score.getKeyQuality() == 0:
      score.setKeyQualty(1)
   elif score.getKeyQuality() == 1:
      score.setKeyQuality(0)

# functions for creative use - utilizes random numbers and built in Mod functionality from the jython library
# take a phrase as an argument 
def invertPhrase(phr):
   Mod.invert(phr)
   return phr

def shufflePhrase(phr):
   Mod.shuffle(phr)
   return phr

def cyclePhrase(phr):
   Mod.cycle(phr)
   return phr

def fillRests(phr):
   Mod.fillRests(phr)
   return phr

def mutatePhrasre(phr): # might need a confirmation step here, otherwise they won't be able to "undo"
   phr2 = Mod.mutate(phr)
   confirmMutation(phr,phr2)

def confirmMutation(phr,phr2,part): # need a pop-up window here
   temp_display = Display("Save Mutation?",300,300)
   view.d.add(temp_display)
 
   if noBttnClicked == True:
      part.addPhrase(phr)  
      score.addPart(part)
   if yesBttnClicked == True:
      phr = phr2
      part.addPhrase(phr)
      score.addPart(part)
   
   view.d.remove(temp_display)

      
   
