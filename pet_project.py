import random

class pet:
    def __init__(self, name, age, joy, smelliness, motivation_to_live, hungriness):
        self.name = name
        self.age = age
        self.joy = joy
        self.smelliness = smelliness
        self.motivation_to_live = motivation_to_live
        self.hungriness = hungriness
    def play(self, joy):
        joy += 10
        activities = ['fetch', "tug o' war, chase"]
        print("You're pet played", activities[random.randint(0,2)], "with you, and gained 10 joy!")
    def wash(self, smelliness):
        smelliness += 10
        print("You're pet finally isn't filthy! It lost 10 smelliness!")
    def therapy(self, motivation_to_live):
        motivation_to_live += 10
        print("You're pet underwent therapy and is no longer emo!  It gained 10 motivation_to_live points!")