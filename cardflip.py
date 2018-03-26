import random

def main():
    global list, userChoiceList, successList
    list = listFormation()
    userChoiceList = []
    successList = []
    printCards()
    flips = 0
    while True:
         if len(successList) == 16:
             print "Number of flips %s" % flips
             break
         userInput()
         printCards()
         flips+=1


def printCards():
    print "---------------------------------------------------------------"
    print "============================================"
    for n in xrange(len(list)):
        if n >= 3 and n % 4  == 0:
            print "\n"
            print "============================================"

        if n in successList:
            print " -----  | ",
        elif n in userChoiceList:
            print "  " + str(list[n]) + "     |  ",
        else:
            print "  "    "     |  ",

    if len(userChoiceList) == 2:
        if list[userChoiceList[0]] == list[userChoiceList[1]]:
            successList.append(userChoiceList[0])
            successList.append(userChoiceList[1])

    print "\n"

def userInput():
    if len(userChoiceList) == 2:
        del userChoiceList[:]

    while True:
        try:
            choice = raw_input("Enter the number [0-15] to flip the card")
            if int(choice) in userChoiceList or int(choice) in successList:
                print "Card is already flipped. Enter another position to flip the card"
            elif int(choice) < 0 or int(choice) > 15:
                print "Enter a number between 0-15"
            else:
                break
        except:
            print "Enter a number"


    userChoiceList.append(int(choice))

def listFormation():
    list = []
    for x in range(4):
        randomList = random.sample(range(1, 5), 4)
        for n in randomList:
            list.append(n)
    random.shuffle(list)
    return list

if __name__ == "__main__":
    main()