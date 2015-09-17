print("Please think of a number between 0 and 100!")
found = False
start = 0
end = 100
while not found :
    guess = (start + end)/2
    print "Is your secret number " + str(guess) + "?"
    #print "Enter 'h' to indicate the guess is too high.",
    #print "Enter 'l' to indicate the guess is too low.",
    #print "Enter 'c' to indicate I guessed correctly.",
    response = raw_input("Enter 'h' to indicate the guess is too high." + " Enter 'l' to indicate the guess is too low." + " Enter 'c' to indicate I guessed correctly. ")
    if response == 'l' :
        start = guess
    elif response == 'h' :
        end = guess
    elif response == 'c' :
        found = True
    else :
        print "Sorry, I did not understand your input."
print "Game over.",
print "Your secret number was: " + str(guess)