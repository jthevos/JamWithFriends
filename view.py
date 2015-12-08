from gui import *
import controller, model

d = Display("Jam With Friends", 1280, 720)

menu = Menu("File")
menuItemList = ["New Jamspace","Open Jamspace","Save Jamspace","Connect Device to Computer","Browse Jamspaces"]
menuFunctionList = [createJamspace, openJamspace, saveJamspace, connectToOSC, browseJams]

menu.addItemList(menuItemList, menuFunctionList)
d.addMenu(menu)

playLine = Line(10,10,10,720, Color.RED,3)
d.add(playLine)

playButton = Button("Play music", controller.playPause) 
d.add(playButton)

addPart1 = Button("+", controller.createPart)
addPart2 = Button("+", controller.createPart)
addPart3 = Button("+", controller.createPart)
addPart4 = Button("+", controller.createPart)

d.add(addPart1)
d.add(addPart2)
d.add(addPart3)
d.add(addPart4)



      