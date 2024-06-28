import random
print("******** Welcome to the game of Rock Paper Scissors ********")
choice = input("Do you want to play :- (Yes/No) ")
u_score = c_score = 0
while choice == "Yes":
    print(f"Current Score\nUser = {u_score}\nComputer Score = {c_score}")
    choices = ["Rock","Paper","Scissors"]
    print(f"Choices = {choices}")
    user_choice = input("Enter Your Choice :- ")
    computer_choice = random.choice(choices)
    if user_choice=="Rock" and computer_choice=="Rock":
        print("Tie")
    if user_choice=="Rock" and computer_choice=="Paper":
        print("Computer Won")
        c_score +=1
    if user_choice=="Rock" and computer_choice=="Scissors":
        print("User Won")
        u_score+=1
    if user_choice == "Paper" and computer_choice == "Paper":
        print("Tie")
    if user_choice == "Paper" and computer_choice == "Scissors":
        print("Computer Won")
        c_score += 1
    if user_choice == "Paper" and computer_choice == "Rock":
        print("User Won")
        u_score += 1
    if user_choice=="Scissors" and computer_choice=="Scissors":
        print("Tie")
    if user_choice=="Scissors" and computer_choice=="Rock":
        print("Computer Won")
        c_score +=1
    if user_choice=="Scissors" and computer_choice=="Paper":
        print("User Won")
        u_score+=1
    choice = input("Do you want to play :- (Yes/No) ")

print("Thankyou")
quit()