class Player:
    def __init__(self):
        self.score = 0
        self.attack_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        self.selected_attack = self.attack_list[0]