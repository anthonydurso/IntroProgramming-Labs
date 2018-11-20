import random     
# Board as a 3x3 matrix
symbol = [ " ", "x", "o" ]
print("TIC TAC TOE ")
board = [0,1,2,
         3,4,5,
         6,7,8]
def printboard():
        print("+-----------+")
        print("|",board[0], '|',board[1], '|',board[2],"|") 
        print("-------------")
        print("|",board[3], '|',board[4], '|',board[5],"|") 
        print("-------------")
        print("|",board[6], '|',board[7], '|',board[8],"|")
        print("+-----------+")
while True:
        area = int(input("Choose an area from 0-8: "))

        if board[area]!= 'X' and board[area] != 'O':
                board[area] = 'X'
        else:
                print("You can not pick this area.")
        printboard()
                                                
while True:
        opponent = random.randint(0,8)

        if board[opponent] != "o" and board[opponent] != "x":
                board[opponent] = "o"
        else:
                print("You can not pick this area.")
                break
