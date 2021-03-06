import time
##Hello Curt Boy!

keyphrase = "The quick brown fox jumps over the lazy dog"


print("Lets see how fast and accurate you can type! Type the phrase '"+ keyphrase + "' You must press enter to submit your phrase. You have 10 seconds.The timer has already started, Start!")
x = input("")

def split(word):
    return list(word)

def typertime():
    count = 1
    numLetters = len(keyphrase)
    numLetters1 = len(keyphrase)
    numInput = len(x)
    lili = split(keyphrase)
    lilo = split(x)
    a = 0
    breaker = 0

    while True:

        for d in range (11):
            time.sleep(1)
            count -= 1
            if count == 0:
                print("Times Up!")
                time.sleep(0.5)
                for s in range(0, numLetters1):
                    if numLetters > numInput or numLetters < numInput:
                        diff = numLetters - numInput
                        diff = abs(diff)
                        for t in range(diff):
                            if numLetters > numInput:
                                lili.pop()
                                numLetters -= 1
                            if numLetters < numInput:
                                lilo.pop()
                                numInput -= 1
                                a -= 1
                for j in range(numLetters):
                    if lili[j] == lilo[j]:
                        a += 1
                        
                if numLetters > 0:        
                    a = a/numLetters1
                    a = a*100
                    a = round(a, 1)
                if numLetters == 0:
                    a = 0
                        
                print("You typed the phrase with " + str(a) + "% accuracy")
                breaker += 1
        if breaker != 0:
            break
    


typertime()







