import zombiedice
import zombiedice as zombiedice
import random


class stopAtTwo: # A bot that stops rolling after it has rolled two brains
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class randomAfterFirst:  # A bot that, after the first roll, randomly decides if it will continue or stop
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        choice = [0, 1]

        while diceRollResults is not None:
            if random.choice(choice) == 1:
                diceRollResults = zombiedice.roll()
            else:
                break


class twoShotguns:  # A bot that stops rolling after it has rolled two shotguns
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class oneToFour:  # A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        roll = [1, 2, 3, 4]
        rolls = random.choice(roll)
        shotguns = 0
        for i in range(rolls):
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class shotgunBrains:  # A bot that stops rolling after it has rolled more shotguns than brains
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns <= brains:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    stopAtTwo(name='Stop at 2 Brains'),
    randomAfterFirst(name='Random Decision'),
    twoShotguns(name='Stop at 2 Shotguns'),
    oneToFour(name='one to four rolls'),
    shotgunBrains(name='shotgun vs brains')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
