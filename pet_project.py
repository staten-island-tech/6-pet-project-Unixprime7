import random

class pet:
    def __init__(self, name, age, joy, smelliness, motivation_to_live, hungriness):
        self.name = name
        self.age = age
        self.joy = joy
        self.smelliness = smelliness
        self.motivation_to_live = motivation_to_live
        self.hungriness = hungriness
    def play(self):
        self.joy += 10
        activities = ['fetch', "tug o' war", "chase"]
        print(self.name, "played", activities[random.randint(0,2)], "with you, and gained 10 joy points!")
    def wash(self):
        self.smelliness -= 10
        print(self.name, "finally isn't filthy! It lost 10 smelliness points!")
    def therapy(self):
        self.motivation_to_live += 10
        print(self.name, "underwent therapy and is no longer emo!  It gained 10 motivation_to_live points!")
    def feed(self):
        self.hungriness -= 10
        foods = ["dead rat", "moldy cheese", "monkey toenails"]
        print(self.name, "ate some", foods[random.randint(0,2)], "and lost 10 hungriness points!")
    def day_pass(self):
        self.age += 1
        self.joy -= 2
        self.smelliness += 2
        self.motivation_to_live -= 2
        self.hungriness += 2
        print(self.name, "is getting old...a day has passed!")
    def death(self):
        if self.age >= 20:
            print("Guess what,", self.name, "was too old and decided life was for noobs!")
            return "dead"
        elif self.joy <= 0:
            print("Imagine not playing with", self.name, "lol, it died btw")
            return "dead"
        elif self.smelliness >= 20:
            print("'A wise pet is one that realizes showering is for the weak' - Your dead pet")
            return "dead"
        elif self.motivation_to_live <= 0:
            print("Unfortunately,", self.name, "has become as heart-breakingly miserable and dead inside as Mr. Whalen, and died while eating a tub of Ben & Jerries on a couch watching anime")
            return "dead"
        elif self.hungriness >= 20:
            junk = ['a pencil case', "a laundry basket", "Eva's foot"]
            print(self.name, "was so desperate it started chewing on", junk[random.randit(0,2)], "before it contracted into a skeleton.  Shame on you.")
    def stats(self):
        stats = [
        {'age': self.age},
        {'joy': self.joy},
        {'smelliness': self.smelliness},
        {'motivation to live': self.motivation_to_live},
        {'hungriness': self.hungriness}
        ]
        return stats
        
pet_name = input("What do you want to name your pet? ")
user_pet = pet(pet_name, 0, 10, 10, 10, 10)
print("Here are the rules:  You can do 1 action each day to try to keep your pet alive.  Once you reach 0 Joy, 0 Motivation to Live, 20 Smelliness, or 20 Hungriness, you DIE! Enjoy :)")
dead = False
while dead == False:
    print("Which action would you like to do? (Case sensitive: Lowercase only)")
    print("[P]lay (+10 Joy)")
    print("[W]ash (-10 Smelliness)")
    print("[T]herapy (+10 Moitivation to Live)")
    action = input("[F]eed (-10 Hungriness) ")
    if action == "p":
        user_pet.play()
    elif action == "w":
        user_pet.wash()
    elif action == "t":
        user_pet.therapy()
    elif action == "f":
        user_pet.feed()
    user_pet.day_pass()
    print(user_pet.stats())
    if user_pet.death() == "dead":
        dead = True
    if dead == False:
        print("Congrats, your pet has lived to see another day!")

