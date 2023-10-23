print(" \n\tRock-Paper-Scissors ")

Options = [ "Rock", "Paper", "Scissors" ]
Outcome = []

Option_1 = "Rock"
Option_2 = "Paper"
Option_3 = "Scissors"   
    
while True:
    new_game = input("\n\tNew game? \t").capitalize()
    if new_game == "Yes":  
        player_1 = input("\nPlayer 1 please enter you option: ").capitalize()
        if player_1 in Options:
            Outcome.append(player_1)
            player_2 = input("Player 2 please enter you option: ").capitalize()
            if player_2 not in Options:
                print("<<< Invalid Option Player 2 >>>")
                break
            else:
                Outcome.append(player_2)
                
                if Outcome[0] == Outcome[1]:
                    print("Draw")
                elif Outcome[0] == Option_1 and Outcome[1] == Option_2:
                    print(" Paper beats Rock - Player 2 WON!")
                elif Outcome[1] == Option_1 and Outcome[0] == Option_2:
                    print(" Paper beats Rock - Player 1 WON!")
                elif Outcome[0] == Option_1 and Outcome[1] == Option_3:
                    print("Rock beats Scissors - Player 1 WON!") 
                elif Outcome[1] == Option_1 and Outcome[0] == Option_3:
                    print("Rock beats Scissors - Player 2 WON!")
                elif Outcome[0] == Option_3 and Outcome[1] == Option_2:
                    print("Scissors beats paper - Player 1 WON!")
                elif Outcome[1] == Option_3 and Outcome[0] == Option_2:
                    print("Scissors beats paper - Player 2 WON!")
                                                      
        elif player_1 not in Options:
            print("<<< Invalid Option Player 1 >>>")
            break
    else:
        print("\n\tGood Bye!")
        break
