import random
import requests
import json

class Player:
    def __init__(self, name):
        self.name = name
        self._points = 0 # TODO: Get from txt file
    def getPoints(self):
        return self._points
    def save(self):

        with open("gamedata.txt", "w") as file:
            file.write(str(self.name) + "\n")
            file.write(str(self._points) + "\n")
            file.write(str(True) + "\n")


class Bot:
    def __init__(self):
        pass
    # ok, I am going to eat too
        # Bro i need take a bath, and eat some food, im hungry
        # ok
    def makeQuestion(self, Player):
        response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy") # look this Website, this response json
        if response.status_code:
            print("New Question!")
            # so , how to make it file with python and write it?
            # txt binary
            loaded = response.json()
        elif not response.status_code:
            print("Something went wrong")
            return 0
        answerList = []
        answersPlayer = []
        n = random.randint(0, 9)
        for i in loaded["results"][n]["incorrect_answers"]:
            answerList.append(i)
        answerList.append(loaded["results"][n]["correct_answer"])
        print(loaded["results"][n]["question"])
        for i in range(1, len(answerList) + 1):
            chosen = random.choice(answerList)
            print(str(i) + ") " + chosen)
            answerList.remove(chosen)
            answersPlayer.append(chosen)
        playerChosen = int(input("Enter number: "))
        if answersPlayer[playerChosen - 1] in loaded["results"][n]["correct_answer"]:
            print("Correct!")
            Player.save()
        else:
            print("Wrong")

if __name__ in "__main__":
    name = input("Enter your name: ")
    p1 = Player(name)
    bot = Bot()
    bot.makeQuestion(p1)