from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Please Enter your name Human!:  ").title()
    
    def choose_attack(self):
        try:
            print("\nPlease select an attack:")
            attack = input('''\n1.Rock 
2. Paper
3. Scissors
4. Lizard
5. Spock
Enter Number of Selection:
            
''')
            self.selected_attack = self.attack_list[int(attack)-1]
        except:
            print("\n Invalid response. Please only use a number between 1-5")
            self.choose_attack()
