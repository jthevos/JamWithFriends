import view, model
from timer

def importSong():
   model.readNewMIDISong()

def getCurrentScore():
   return model.score

def viewInstrumentParts(): # used to view all parts currently in the score
   model.viewParts()

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
   

# delete functions for different levels of granularity 
def deleteSubPhrase(part, phr):
   phr.empty()
   return part    
     
def deleteSubPart(score,part):
   part.empty()
   print part.getTitle() + "has been deleted."
   return score

# to be called for the loop button   


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
def playPause():
   material = model.score
   if material.isPlaying():
      matieral.pause()
   elif not material.isPlaying():
      material.play()
      
# need to add actual volume control here   
def changeVolume(new_value):
   slider1.setValue(new_value)




# possibly link this to a slider that goes from -7 to 7 which will
# correspond to flats and sharps with 0 being C in major and A in minor
# assumes major for now.
def changeKeySignature(signature):
   score.setKeySignature(signature)
   return score