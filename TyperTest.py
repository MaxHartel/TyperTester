import time

keyphrase = "The quick brown fox jumps over the lazy dog"


print("Lets see how fast and accurate you can type! Type the phrase '"+ keyphrase + "' You have 7 seconds")
x = input("")

def split(word):
    return list(word)

def typertime():
    count = 7
    numLetters = len(keyphrase)
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
                for s in range(0, numLetters):
                    if lili[s] == lilo[s]:
                        a += 1
                a = a/numLetters
                        
                print("You typed the phrase with " + str(a) + "% accuracy")
                breaker += 1
        if breaker != 0:
            break
    


typertime()
x = input("")






