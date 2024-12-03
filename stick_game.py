'''Author:Thomas Cherian
   date: 3-12-24
   python program:To create a stick game in python'''
print("welcome to stick game")
print("Two players take turns to play the game. Each player picks one set of sticks during his turn. \n RULES \n"
      "A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser.\n "
      "The number of sticks in the set is to be input.")
def stick_game():
   player1=input("enter name of player1:")
   player2=input("enter name of player2:")
   sticks=16
   print(f"number of sticks remaining ={sticks}")
   while sticks>0:
       score1=int(input(f"{player1},chose 1,2,3 sticks:"))
       if score1>3 or score1<1:
           print("invalid input game over ")
           break
       sticks = sticks - score1
       print(f"number of sticks remaining ={sticks}")
       if sticks<=0:
           print(f"{player1} lost. better luck next time")
           break
       score2=int(input(f"{player2},chose 1,2,3 sticks:"))
       if score1>3 or score1<1:
           print("invalid input game over ")
           break
       sticks = sticks - score2
       print(f"number of sticks remaining ={sticks}")
       if sticks<=0:
           print(f"{player2} lost. better luck next time")
           break

print(stick_game())