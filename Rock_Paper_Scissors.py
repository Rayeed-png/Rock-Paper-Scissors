import random
print("Hello, I want to challenge you to a clash of rock, paper, scissors! First to 5 points win!")
name = input("Please tell me your name: ")
print(f"Nice to meet you {name}.")
skill = input(f"{name} are you skilled in this game please tell me yes or no: ")
if skill == "yes":
    print(f"I am so scared of you {name} right now.")
elif skill == "no":
    print(f"I will remember you {name} as an easy fight.")
else:
    print("WILL YOU PLEASE TELL ME")
    input(f"{name} are you skilled in this game please tell me yes or no?")
print("Thank you for your details lets begin!")
robot_score = 0
player_score = 0
while True: 
    choice = input(f"{name} choose either rock, paper, or scissors: ")
    if choice != "rock" and choice != "paper" and choice != "scissors":
        print("PLZ CHOOSE EITHER OF THE 3")
        continue
    random_choice = random.randint(1,3)
    robot_choice = ""
    if random_choice == 1:
        robot_choice = "rock"
    elif random_choice == 2:
        robot_choice = "paper"
    elif random_choice == 3:
        robot_choice = "scissors"
    print(f"I chose {robot_choice}")
    if choice == robot_choice:
        print("TIE")
    elif choice == "rock" and robot_choice == "paper":
        print("Sorry I won that one")
        robot_score = robot_score + 1
        print(f"My Points = {robot_score} | Your Points = {player_score}")
    elif choice == "paper" and robot_choice == "scissors":
        print("Sorry I won that one")
        robot_score = robot_score + 1
        print(f"My Points = {robot_score} | Your Points = {player_score}")
    elif choice == "scissors" and robot_choice == "rock":
        print("Sorry I won that one")
        robot_score = robot_score + 1
        print(f"My Points = {robot_score} | Your Points = {player_score}")
    else:
        print(f"{name} you've earned a point")
        player_score = player_score + 1
        print(f"My Points = {robot_score} | Your Points = {player_score}")
    if robot_score == 5:
        print(f"HAHAHA YOU'VE LOST {name}!!!")
        break
    if player_score == 5:
        print(f"{name} HOW DID YOU BEAT ME!!!")
        break
  
