from music import *
from random import *
from gui import *

phrase_Array = []
global previousState

def smartUndo():
   # reinitialize previousState
   # this might be more difficult to implement than it's worth
   
   
def changeNote(note,y_position):
   # event = mouseRelease or release touch on phone
   # y_position is the vertical position of the new dragged note
   # y can be both positive and negative to indicate increasing
   # and decreasing pitch
   startingPitch = note.getPitch()
   newPitch = note.setPitch(startingPitch + y_position)
   return newPitch

def duplicateNote(note):
   note2 = note.copy()
   note2.setDuration(note.getDuration()/2)
   return [note2, note2]

def changeNoteDuration(note,rthm_value):
   return note.setDuration(rthm_value)

def addNote(pitch,duration,phrase):
   # not sure if I need to be utilizing self
   # for the scale of editing we're doing, I don't think 
   # we'll be utilizing the part level until the file is finished
   # i.e., it appends all the phrases once "save" is hit
   
   previousState = phrase
   phrase2 = phrase.copy()
   note = Note(pitch, duration)
   self.phrase2.addNote(note)
   #phrase_Array.

def preSaveHousekeeping():
   # 
   
   
def saveState():
   
