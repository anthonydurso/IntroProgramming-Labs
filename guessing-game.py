def guessGameTitle():
    ##print title
    print("Python Guessing Game")

guessGameTitle()

animalName="lion"

while True:
    answer = input("Guess the animal I am thinking of : ")
    if answer.lower() == animalName.lower():
        print("Thats it!!")
        break
    elif answer == "quit":
        break
    else:
        print("Thats not it try again")
