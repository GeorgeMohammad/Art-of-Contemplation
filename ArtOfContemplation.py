import time
import random
import datetime
#This program is a timer that helps you learn Aristotle's Art of Contemplation.


#computes the time over a range
def GetTime():
    finished = False
    startTime = time.time()
    while (not(finished)):
        quitCheck = input("q)uit, timer has started, " + \
                          "anything else to continue").lower()
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

#Recordes a list, dataSet, whose length is equal to colTitles length
#in a csv file.
def Logger(dataSet):
    colTitles = ["TimerValue", "Date", "QualityEvaluation", "FocusEvaluation"]
    colTitleFlag = True
    try:
        fileI = open("log.csv", "r")
        fileContents = fileI.read()
        fileI.close()
        open("log.csv", "r")
        for i in colTitles:
            if (i not in fileContents):
                raise
    except:
        fileO = open("log.csv", "w")
        for i in colTitles:
            fileO.write(i + ",")
        fileO.write("\n")
        fileO.close()
    finally:
        if (colTitleFlag):
            fileO = open("log.csv", "a")
            if ((type(dataSet) is list) and (len(dataSet) == len(colTitles))):
                for i in dataSet:
                    if (type(i) is str):
                        fileO.write(i + ",")
                    else:
                        print (i, "is not a string")
                fileO.write("\n")
            fileO.close()

quitCheck = input("q)uit, a)dd medal entry, d)elete medal entry, L)og data")
medalList = []

#main menu
while (quitCheck.lower() != "q"):
#add medal list entry
    if (quitCheck.lower() == "a"):
        userMedalEntry = input("Entry: ")
        medalList.append(userMedalEntry)
#delete medal list entry
    if (quitCheck.lower() == "d"):
        entry2Delete = input("Enter an entry to delete: ")
        if (entry2Delete in medalList):
            medalList.remove(entry2Delete)
        else:
            print("That value isn't in the list.")
#Create log entry
    if (quitCheck.upper() == "L"):
        timerVal = str(GetTime())
        date = input("Enter a date (dd/mm/yyyy): ")
        qualityEvaluation = input("How did it go in terms of quality(1-100): ")
        focusEvaluation = input("How was your focus (1-100): ")
        dataSet = [timerVal, date, qualityEvaluation, focusEvaluation]
        Logger(dataSet)
    quitCheck = input("q)uit, a)dd medal entry, d)elete medal entry, L)og data")
