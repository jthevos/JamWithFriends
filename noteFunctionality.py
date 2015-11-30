from music import *
from random import *
from gui import *

phrase_Array = []
global previousState

def smartUndo(eventList):
   eventList[0]
# event = mouseRelease
# y_position is the vertical position of the new dragged note
# y can be both positive and negative to indicate increasing
# and decreasing pitch
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

# not sure if I need to be utilizing self
# for the scale of editing we're doing, I don't think 
# we'll be utilizing the part level until the file is finished
# i.e., it appends all the phrases once "save" is hit
def addNote(pitch,duration,phrase):
   previousState = phrase
   phrase2 = phrase.copy()
   note = Note(pitch, duration)
   self.phrase2.addNote(note)
   #phrase_Array.

def preSaveHousekeeping():
   
   
   
def saveState():
   preSaveHousekeeping()
   
   workingScore = 0

