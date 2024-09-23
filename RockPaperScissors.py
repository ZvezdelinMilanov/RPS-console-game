import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_choice = input("Choose between \n[1]Rock \n[2]Paper \n[3]Scissors: ")
if player_choice == "1":
    player_choice = rock
elif player_choice == "2":
    player_choice = paper
elif player_choice == "3":
    player_choice = scissors
else:
    raise SystemExit("Oops - > Invalid Input. Can you try again ?")


pc_random_number = random.randint(1, 3)
pc_choice = ''
if pc_random_number == 1:
    pc_choice = rock
elif pc_random_number == 2:
    pc_choice = paper
elif pc_random_number == 3:
    pc_choice = scissors

print(f"The computer chose {pc_choice}.")

if (player_choice == rock and pc_choice == scissors) or \
        (player_choice == paper and pc_choice == rock) or \
        (player_choice == scissors and pc_choice == paper):
    print("You've beaten your own computer !!!")
elif player_choice == pc_choice:
    print("Draw!")
else:
    print("You lost to a computer!")


