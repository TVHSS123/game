print("""

░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
""")
print("Welcome To My island\n")
print("There are two doors in the front of you. 🚪 a red door and 🚪 ablue door")

door = input("Which door do you want to open? : ")

if door.lower() == "red":
  print("Greet! Now You Entered a Room")
  print("You Found Three Boxes: 🎁 white, 🎁 black, 🎁 green")
  door_2 = input("which box do you open? : ")
  
  if door_2.lower() == "green":
    print("Greet! You Found The Treasure")
  elif door_2.lower() == "white":
    print("Oops! You Opend a box filled with snakes")
  elif door_2.lower() == "black":
    print("Oops! You Opend a box filled spiders")
  else:
    print("\nError, Inviled Choice")

elif door.lower() == "blue":
  print("\nOops! You Chose The crocodile door.")
  print("Game Over.")
else:
  print("\nError, Inviled choice")
