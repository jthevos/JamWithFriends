from osc import *
from music import *

oscIn = OscIn(57110) #port number is argument; to send OSC message, you need IP and port #

def test(message):
   print "confirmed reciept"

def completeTest(message):
   OSCaddress = message.GetAddress()
   args = message.getArguments()
   
   #print OSC message time and address
   print
   print "OSC Event: "
   print "OSC In - Address: ", OSCaddress,
   
   #dir(oscIn) will give a dictionary of possible key:value pairs
   for i in range(len(args)):
      print ", Argument " + str(i) + ": " +str(args[i]),
   print
   
oscIn.onInput("/helloWorld",test)

oscIn.onInput("/.*", completeTest)

# how to send a message to manaris computer
# from osc import *
# oscOut = OscOut("10.0.1.2","57110")
# oscOut.sendMessage("/John","Thevos")