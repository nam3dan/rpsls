from human import Human
from ai import AI
import time

master_rule_dict = {"Rock":{"Scissors":" Crushes ","Lizard":" Crushes"},
                    "Paper":{"Rock":" Covers ","Spock":" Disproves "},
                    "Scissors":{"Paper":" Cuts ","Lizard":" Decapitates "},
                    "Lizard":{"Spock":" Poisons ","Paper":" Eats "},
                    "Spock":{"Scissors":" Smashes ", "Rock": " Vaporizes "}
                    }

class Game:
    def __init__(self):
        self.intro()
        self.rounds = self.return_rounds()
        self.players = self.number_of_humans()
        self.print_game_rules()
    
    def intro(self):
        print("\nHello and Welcome to ROCK, PAPER, SCISSORS, LIZARD, SPOCK!")
    
    def number_of_humans(self):
        try:
            human_count = int(input("\nPlease enter number of humans (0|1|2): "))
        except:
            print("Invalid Entry. Please type only either 1, 2 0r 3")
            self.number_of_humans()
        if human_count == 0:
            self.player1 = AI()
            self.player2 = AI()
        elif human_count == 1:
            self.player2 = AI()
            print("\nHello, I'm " + self.player2.name + ". I'll be your competitor today.")
            self.player1 = Human("player 1")
        else:
            self.player1 = Human("player 1")
            self.player2 = Human("player 2")
        player_list = []
        player_list.append(self.player1)
        player_list.append(self.player2)
        return player_list
    
    def return_rounds(self):
        try:
            number_of_rounds = int(input("\nHow many rounds would you like to play?: "))
        except:
            print("Invalid Entry")
            self.rounds
        return number_of_rounds
    
    def print_game_rules(self):
        print('''The Rules of the Game are simple:
You will from one of 5 options:
1. Rock
2. Paper
3. Scisors
4. Lizard
5. Spock''')
        time.sleep(5)
        print('''Similar to RPS, here are the attack hierarchy:

Rock crushes Scissors
Scissors cuts Paper 
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock

Best out of ''' + str(self.rounds) + ''' wins.''')
    
    def run_game(self):
        round_counter = 0
        while self.players[0].score < self.rounds/2 and self.players[1].score < self.rounds/2:
            round_counter += 1
            print('\nRound ' + str(round_counter))
            self.player1.choose_attack()
            self.player2.choose_attack()
            p1_attack = self.player1.selected_attack
            p2_attack = self.player2.selected_attack
            try:
                action = master_rule_dict[p1_attack][p2_attack]
                self.player1.score += 1
                winner = self.player1.name
            except:
                action = master_rule_dict[p2_attack][self.player1.selected_attack]
                self.player1.score += 1
                winner = self.player2.name
            else:
                winner = "voie"
            if winner == "void":
                print("\nYou both chose " + p1_attack +". This round is a tie")

