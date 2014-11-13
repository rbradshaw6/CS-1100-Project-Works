#Robert Bradshaw and John S. Yi
#underwaterbasketweaving@gatech.edu
#We worked on the homework assignment alone, using only this semester's course materials."


from Myro import *
from Graphics import *
import math
init()
def turn():
    x = heads()
    if x == True:
        setLED("right","on")
        wait(.3)
        setLED("right","off")
        turnRight(1,1.2)
    elif x == False:
        setLED("left","on")
        wait(.3)
        setLED("left","off")
        turnLeft(1,1.2)

setPicSize("small")
image = takePicture()



def findColor(image):
   # pixel = getPixel(image, 256/2, 192/2)
    #r,g,b = getRGB(pixel)
    greenProp = 0
    yellowProp = 0
    redProp = 0
    whiteProp = 0

    for pixel in getPixels(image):
        r,g,b = getRGB(pixel)
        if g > r and g > b:
            greenProp = greenProp + 1

        elif r > b and g > b:
            yellowProp = yellowProp + 1

        elif r > b and r > g:
            redProp = redProp + 1

        elif r > 160 and g > 160 and b > 160:
            whiteProp = whiteProp + 1



    if greenProp > yellowProp and greenProp > redProp and greenProp > whiteProp:
        forward(1,2)#image is green
        return('green')
    elif yellowProp > greenProp and yellowProp > redProp and yellowProp > whiteProp:
        forward(.5,2) #image is yellow
        return('yellow')
    elif redProp > yellowProp and redProp > greenProp and redProp > whiteProp:
        stop() #image
        return('red')
        beep(1,800)
    elif whiteProp > yellowProp and whiteProp > greenProp and whiteProp > redProp:
        turn()
        return('white')
##########################################################################################################################

def stopLight():
    greenProp = 0
    yellowProp = 0
    redProp = 0
    whiteProp = 0

    swag = True

    while swag == True:
        image = takePicture()
        setPicSize("small")
        for pixel in getPixels(image):
            r, g, b = getRGB(pixel)
            if g > r and g > b:

                #print(pixel)
                greenProp = greenProp + 1
        
            elif r > b and g > b:

                #print(pixel)
                yellowProp = yellowProp + 1
        
            elif r > b and r > g:

                redProp = redProp + 1
        
            elif r > 160 and g > 160 and b > 160:
                whiteProp = whiteProp + 1



        if greenProp > yellowProp and greenProp > redProp:
            forward(1,2)#image is green
            print("green")
            wait(1)
        elif yellowProp > greenProp and yellowProp > redProp:
            forward(.5,2) #image is yellow
            print("yellow")
            wait(1)
        elif redProp > yellowProp and redProp > greenProp:
             #image is red and stops
            beep(1,800)
            print("red")
            return("red")
            swag == False
            break
            stop()
        elif whiteProp > yellowProp and whiteProp > greenProp and whiteProp > redProp:
            turn()
            print("white")
            wait(1)

