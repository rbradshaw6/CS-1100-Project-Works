#Robert Bradshaw and Laura McKenzie
#rbradshaw6@gatech.edu
# We for pair programming assignments) worked on the homework assignment alone, using only this semester's course materials.

from Myro import *
from Graphics import *
f = open('myMovements.txt','w')

win = Window()
def dankControlsBro(win,event):
    f = open("myMovements.txt", 'a')
    if event.key == "Up":
        f.write("forward\t")
        f.write("\t.1\t")
        dank = getLight("left")/(getLight("right") + getObstacle("right"))
        dank = str(dank)
        f.write(dank +"\n")
        f.close()
        forward(1,.1)

    if event.key == "Down":
        f.write("backward")
        f.write("\t.1\t")
        dank = getLight("left")/(getLight("right") + getObstacle("right"))
        dank = str(dank)
        f.write(dank +"\n")
        f.close()
        backward(1,.1)

    if event.key == "Right":
        f.write("turnRight")
        f.write("\t.1\t")
        dank = getLight("left")/(getLight("right") + getObstacle("right"))
        dank = str(dank)
        f.write(dank +"\n")
        f.close()
        turnRight(1,.1)

    if event.key == "Left":
        f.write("turnLeft")
        f.write("\t.1\t")
        dank = getLight("left")/(getLight("right") + getObstacle("right"))
        dank = str(dank)
        f.write(dank +"\n")
        f.close()
        turnLeft(1,.1)

    if event.key == "b":
        f.write("beep")
        f.write("\t.1\t\n")
        f.close()
        beep(.1,800)


onKeyPress(dankControlsBro)

def collectData(dankFileName, derection):
    count1 = 0
    count2 = 0
    count3 = 0
    swagFile = open(dankFileName, "r")

    text = swagFile.readline()


    while len(text) > 0:
        ind = text.split()
        if ind[1] == ".1":
            count1 = count1 + 1
        if ind[0] == "beep":
            count2 = count2 + 1
            count1 = count1 - 1
        if ind[0] == derection:
            count3 = count3 + 1
        text = swagFile.readline()
    answer = "Ya boi Scribby traveled for " + str(count1) + " seconds, beeping " + str(count2) + "times. Ya boi Scribby moved" + str(derection) + str(count3) + "times."
    print(answer)
    return(answer)
    swagFile.close()

def replay(dankFileName):
    swag = open(dankFileName, "r")
    yolo = swag.readline()
    while len(yolo) > 0:
        sweg = yolo.split()
        iCryEvryTime = float(sweg[1])
        if sweg[0] == "forward":
            forward(1,iCryEvryTime)

            print("going forward again?")

        if sweg[0] == "backward":
            backward(1,iCryEvryTime)
            print("going backward again?")

        if sweg[0] == "turnRight":
            turnRight(1,iCryEvryTime)
            print("turnin' right again?")

        if sweg[0] == "turnLeft":
            turnLeft(1,iCryEvryTime)
            print("turnin' left again?")

        if sweg[0] == "beep":
            beep(.1,800)
            print("beepin' again?")
        yolo = swag.readline()


    swag.close()


#dankprogramzbro