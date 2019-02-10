import time
import random
#This program is a timer that helps you learn Aristotle's Art of Contemplation.


#computes the time over a range
def GetTime():
    finished = False
    startTime = time.time()
    while (not(finished)):
        quitCheck = input("q)uit, anything else to continue").lower()
        if (quitCheck == 'q'):
            finished = True
    endTime = time.time()
    timeDifference = endTime - startTime
    return timeDifference

#print(GetTime())

#input: list of encouraging statements.
def Encourager(encouragementList):
    if (type(encouragementList) is list):
        randomIndexVal = random.randrange(1, len(encouragementList))
        return encouragementList[randomIndexVal]
    else:
        print ("Invalid Input. Must input a list. Exiting")

    #return "Error"
#outcome: a random item from the inputted list.

#input: 1 data item
def FileWriter (dataPoint):
    if (type(dataPoint) is str):
        fileO = open("log.csv", "a")
        fileO.write(dataPoint)
    else:
        print ("Invalid Input. Enter a string.")
#outcome: writes the inputted data point to a file named log.csv.

#returns the contents of log.csv as a list
def FileReader():
    try:
        open("log.csv", "r")
    except:
        print ("No file named log.csv")
    else:
        fileI = open("log.csv", "r")
        fileList = fileI.read()
        return fileList

#removes an item from a list.
def ItemRemover(targetVal, targetList):
    if (type(targetList) is list):
        index = targetList.index(targetVal)
        del targetList[index]
    else:
        print ("Invalid Input. Not a list")


##The following is just test code.
##testList = [1, 2, 3]
##print(Encourager(testList))
##print("String Encourager Test: ", Encourager("f"))
##print("Integer Encourager Test: ", Encourager(1))
##ItemRemover(1, testList)
##ItemRemover(2, "k")
##print (testList)
##FileWriter("\ntest\n")
##FileWriter(1)
##fileList = FileReader()
##print (fileList)

