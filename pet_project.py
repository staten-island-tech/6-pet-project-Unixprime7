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
        print("You're pet played", activities[random.randint(0,2)], "with you, and gained 10 joy points!")
    def wash(self, smelliness):
        smelliness += 10
        print("You're pet finally isn't filthy! It lost 10 smelliness points!")
    def therapy(self, motivation_to_live):
        motivation_to_live += 10
        print("You're pet underwent therapy and is no longer emo!  It gained 10 motivation_to_live points!")
    def feed(self, hungriness):
        hungriness += 10
        foods = ["dead_rat", "moldy_cheese", "monkey_toenails"]
        print("You're pet ate some", foods[random.randit(0,2)], "and lost 10 hungriness points!")
    def grow_up(self, age):
        age += 1
        print("You're pet is getting old...It grew up 1 year!")
    def death(self, age, joy, smelliness, motivation_to_live, hungriness):
        if age == 20:
            print("Guess what, your pet was too old and decided life was for noobs!")
            return age, joy, smelliness, motivation_to_live, hungriness
        elif joy == 0:
            print("Imagine not playing with your pet lol, it died btw")
            return age, joy, smelliness, motivation_to_live, hungriness
        elif smelliness == 150:
            print("'A wise pet is one that realizes showering is for the weak' - Your dead pet")
            return age, joy, smelliness, motivation_to_live, hungriness
        elif motivation_to_live == 0:
            print("Unfortunately, your pet has become as heart-breakingly miserable and dead inside as Mr. Whalen, and died while eating a tub of Ben & Jerries on a couch watching anime")
            return age, joy, smelliness, motivation_to_live, hungriness
        elif hungriness == 150:
            print("As you can see, your pet has literally had all of its tissue, ligaments, and muscle disintegrate from the lack of ")