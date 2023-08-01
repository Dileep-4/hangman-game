word = "dileep"
lettersguessed = ""
lifelines = 3
hint = "its a name of one boy "
while lifelines>0:
    guess = input("enter a character: ")
    if guess==word:
        print("correct, you won the game")
    elif guess in word :
        print("correct, some other words are also there in word")
    else:
        lifelines -= 1
        print("incorrect there is no match in word",guess,lifelines,"turns left")
    lettersguessed += guess
    wrongcount = 0
    for letter in word:
        if letter in lettersguessed:
            print(letter,end="")
        else:
            print("_",end="")
            wrongcount += 1
    if wrongcount ==0:
        print(" is secret word you won the game")
        break
else:
    print("sorry, you lost the game")