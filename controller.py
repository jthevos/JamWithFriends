import view, model

# Basic addition of parts based on instrument. 
# Only 5 are included as of to serve as the MVP
# Channel restrictions are observed.
def itemSelected(argument):
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

# unsure as to whether or not the display needs to be passed
# has been included for now
def createJamspace(display):
   print "jamspace created"

def openJamspace():
   print "jamspace opened"

def saveJamspace(activeSession):
   print "Jamspaced Saved!!"

def connectToOSC(ipAddrComp,ipAddrPhone):
   print "Phone is connected at " + ipAddrPhone + " and the comp is at " + ipAddrComp

def browseJams():
   print "Coming soon!"
   
def createPart():
   part = Part()
   return part

# delete functions for different levels of granularity 
def deleteSubPhrase(part, phr):
   phr.empty()
   return part    
     
def deleteSubPart(score,part):
   part.empty()
   print part.getTitle() + "has been deleted."
   return score

# to be called for the loop button   
def copyPart(part):
   Mod.repeat(part,1)
   return part

def copyPhrase(phr):
   Mod.repeat(phr,1)
   return phr

#Plays full score from the beginning
def restartTrack(score):
   Play.midi(score)
   startPlayLine()

def startPlayLine():
   playLine = Line(10,10,10,720, Color.RED,3)
   view.d.add(playLine)
# Should the composer decide to change the instrument of an existing part, 
# they can do so with this.   
def changeInstrument(part,new_instrument):
   part.setInstrument(new_instrument)

# Alternates between play and pause depending on which is active      
def playPause(material):
   if material.isPlaying():
      matieral.pause()
   elif not material.isPlaying():
      material.play()
      
# need to add actual volume control here   
def changeVolume(new_value):
   slider1.setValue(new_value)

# takes a default score in the root file directory 
# clones it, and the cloned file will be what is manipulated throughout
# returns the new score       
def readNewMIDISong():
   score = Score()              # create an empty score
   Read.midi(score, "song.mid") # read MIDI file into it
   score2 = score.copy()
   
   return score2

# flips between major and minor 
def changeQuality(quality):
   if score.getKeyQuality() == 0:
      score.setKeyQualty(1)
   elif score.getKeyQuality() == 1:
      score.setKeyQuality(0)
      
   return score

# possibly link this to a slider that goes from -7 to 7 which will
# correspond to flats and sharps with 0 being C in major and A in minor
# assumes major for now.
def changeKeySignature(signature):
   score.setKeySignature(signature)
   return score