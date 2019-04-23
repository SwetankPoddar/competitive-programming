testCases = int(input())

#Generate new dict
def getNewDict():
    instances = {'c':0,'o':0,'d':0,'e':0,'h':0,'f':0}
    return instances

######
for x in range(testCases):
    numberOfWords = int(input())
    letters = getNewDict()
    for y in range(numberOfWords):
        word = input()
        for letter in word:
            ##Count the number of letters
            if(letters.get(letter) != None):
                letters[letter] +=1
    #Count the number of 'codechef' possible

    numberOfTimesPossible = 0
    while True:
        #Check if all the letters exist
        if( letters['c'] >=2 and letters['o'] >=1 and letters['d'] >=1 and letters['e'] >=2 and letters['h'] >=1 and letters['f'] >=1):
            letters['c'] -= 2
            letters['o'] -= 1
            letters['d'] -= 1
            letters['h'] -= 1
            letters['e'] -= 2
            letters['f'] -= 1
            numberOfTimesPossible +=1
        else:
            break
    print(numberOfTimesPossible)
######
