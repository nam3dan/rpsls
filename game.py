from human import Human
from ai import AI
import time

master_rule_dict = {"Rock":{"Scissors":" Crushes ","Lizard":" Crushes "},
                    "Paper":{"Rock":" Covers ","Spock":" Disproves "},
                    "Scissors":{"Paper":" Cuts ","Lizard":" Decapitates "},
                    "Lizard":{"Spock":" Poisons ","Paper":" Eats "},
                    "Spock":{"Scissors":" Smashes ", "Rock": " Vaporizes "}
                    }

def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            return user_input


class Game:
    def __init__(self):
        self.intro()
        self.rounds = self.return_rounds()
        self.players = self.number_of_humans()
        self.print_game_rules()
    
    def intro(self):
        print("\nHello and Welcome to ROCK, PAPER, SCISSORS, LIZARD, SPOCK!")
    
    def number_of_humans(self):
        human_count = min(input_number("\nPlease enter number of humans (0|1|2): "),2)
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
        number_of_rounds = max(input_number("\nHow many rounds would you like to play? : "),3)
        return number_of_rounds
    
    def print_game_rules(self):
        print('''\n\nThe Rules of the Game are simple:
You will from one of 5 options:
1. Rock
2. Paper
3. Scisors
4. Lizard
5. Spock
''')
        time.sleep(5)
        print('''\nSimilar to RPS, here are the attack hierarchy:

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
        time.sleep(5)

    def run_game(self):
        round_counter = 0
        tie_counter = 0
        while self.players[0].score < self.rounds/2 and self.players[1].score < self.rounds/2:
            round_counter += 1
            print('\nROUND ' + str(round_counter))
            self.player1.choose_attack()
            self.player2.choose_attack()
            p1_attack = self.player1.selected_attack
            p2_attack = self.player2.selected_attack
            print('\n{} chose {}'.format(self.player1.name, p1_attack))
            print('\n{} chose {}'.format(self.player2.name, p2_attack))
            if p1_attack == p2_attack:
                winner = "void"
                tie_counter += 1
            else:
                try:
                    action = master_rule_dict[p1_attack][p2_attack]
                    self.player1.score += 1
                    winner = self.player1.name
                except:
                    action = master_rule_dict[p2_attack][p1_attack]
                    self.player2.score += 1
                    winner = self.player2.name
            if winner == "void":
                print("\nYou both chose " + p1_attack +". This round is a tie.")
            elif winner == self.player1.name:
                print("\n{}{}{}. {} wins!".format(p1_attack,action,p2_attack,winner))
            else:
                print("\n{}{}{}. {} wins!".format(p2_attack,action,p1_attack,winner))
            time.sleep(2)
            print('\nCurrent Score: \n' + self.player1.name + ' : ' + str(self.player1.score) + '\n' + self.player2.name + ''' : ''' + str(self.player2.score))
            time.sleep(3)
        if self.player1.score > self.player2.score:
            winner = self.player1.name
            score = str(self.player1.score)
        else:
            winner = self.player2.name
            score = str(self.player2.score)
        
        print("\n{} WINS!!!!! {} won {} games out of {}. There were {} ties and {} total rounds.\n".format(winner.upper(),winner,score,self.rounds, tie_counter, round_counter))

