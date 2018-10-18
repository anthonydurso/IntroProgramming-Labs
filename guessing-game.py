def guessGameTitle():
    ##print title
    print("Python Guessing Game")

guessGameTitle()

animalName="lion"

while True:
    answer = input("Guess the animal I am thinking of : ")
    if answer == animalName:
        print("Thats it!!")
        break 
    else:
        print("Thats not it try again")
