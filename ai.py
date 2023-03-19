from player import Player
import random

ai_name_list = ["Sheldon","Leonard","Penny","Howard","Raj","Amy","Bernadette"]

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = ai_name_list.pop(ai_name_list.index(ai_name_list[random.randint(0,len(ai_name_list)-1)]))
        
    def choose_attack(self):
        self.selected_attack = self.attack_list[random.randint(0,len(self.attack_list)-1)]