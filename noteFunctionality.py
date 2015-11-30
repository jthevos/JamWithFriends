from music import *
from random import *
from gui import *

# event = mouseRelease
# y_position is the vertical position of the new dragged note
def changeNote(note,y_position):
   startingPitch = note.getPitch()
   newPitch = note.setPitch(startingPitch + y_position)
   return newPitch

def duplicateNote(note):
   note2 = note.copy()
   note2.setDuration(note.getDuration()/2)
   return [note2, note2]

def changeNoteDuration(note,rthm_value):
   return note.setDuration(rthm_value)



