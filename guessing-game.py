def guessGameTitle():
    ##print title
    print("Python Guessing Game")

guessGameTitle()

animalName="lion"

while True:
    answer = input("Guess the animal I am thinking of : ")
    if answer.lower()== animalName.lower():
        print("Thats it!!")
        answerOne = input("Do you like this animal?")
        if answerOne == "Yes"[0].lower():
            print("Nice!")
        else answerOne == "No"[0].lower():
            break
    elif answer == "Quit"[0].lower():
        break
    else:
        print("Thats not it try again")

