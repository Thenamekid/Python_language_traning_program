import random, time

language = "French" # what will be displayed, cange if you want
words = ["hello", "thank you", "yes", "no", "book"] # this is case sensative
facits = ["bonjour", "merci", "oui", "non", "livre"] # change this and the words to what words you want to be quized on
old_words = words.copy()
old_facits = facits.copy() 

def reset(): # to reset the wrong o meter
    global wrong_o_meter
    wrong_o_meter = 0

reset()
        
while True:
    if len(words) != 1: # make the random word to a var so you can reuse it for the facit
        random_numb =  random.randint(0, len(words) - 1)
    else:
        random_numb = 0
    
    word = words[random_numb] 
    facit = facits[random_numb]
    answer = input('What is: "' + word + '" in ' + language + '? ')
    
    if answer != facit:
        print("WRONG!!! The answer was:", facit) # you can remove it saying the facit if you want
        wrong_o_meter = wrong_o_meter + 1
        time.sleep(0.5)
        input("Do you want to continue (just press enter if so)? ")
        loop = 0
        while True: # move the user so they can't see answer
            loop = loop + 1
            print("\n\n\n\n\n\n\n\n\n\n")
            if loop == 4:
                break
    else:
        print("Wow, thats correct. You said:", answer)

        if len(words) <= 1:
            time.sleep(1)
            print("Nice, you have gone thruogh all your words!")
            time.sleep(1)
            print("Good job :)")
            if wrong_o_meter > 0:
                time.sleep(1)
                print("Though you did do", wrong_o_meter, "errors...")
            else:
                print("You didn't do any wrong spellings!")
            time.sleep(2)
            print("Restarting...")
            time.sleep(2)
            loop = 0
            while True: # move the user so they can't see previous answer
                loop = loop + 1
                print("\n\n\n\n\n\n\n\n\n\n")
                if loop == 5:
                    break
            reset()

            words = old_words.copy() # copy the words to what you set them to in the beigining
            facits = old_facits.copy() # same for the facit
        else: # if the words and facits have not gone down to under 2
            words.remove(word) # remove the word we randomly chose
            facits.remove(facit) # and the same facit
