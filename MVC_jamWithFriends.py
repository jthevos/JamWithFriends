from gui import *
from controller import *

d = Display("Jam With Friends", 1280, 720)

menu = Menu("File")
menuItemList = ["New Jamspace","Open Jamspace","Save Jamspace","Connect Device to Computer","Browse Jamspaces"]
menuFunctionList = [createJamspace, openJamspace, saveJamspace, connectToOSC, browseJams]

menu.addItemList(menuItemList, menuFunctionList)
d.addMenu(menu)

playLine = Line(10,10,10,720, Color.RED,3)
d.add(playLine)

# def sendDisplayToController(display):
 #  return display

#slider1 = Slider(VERTICAL, 0, 127, 50, changeVolume) 

#button1 = Button("Play music", playMusic) 
#button2 = Button("Pause music", pauseMusic)

   
#ddl1 = DropDownList(["Piano", "Guitar", "Drums", "Bass","Gunshot"], itemSelected)


      