from board2 import *
from random import *
import matplotlib.pyplot as plt

class Player():
    def __init__(self, name, money = 1500, case = 0):
        self.name = name
        self.money = money
        self.case = case

def create_players(NbrPlayer):
    player_list = []
    for i in range(NbrPlayer):
        player_list.append(Player(str(i)))

    return player_list

def game(NbrPlayer):
    player_list = create_players(NbrPlayer)

    for i in range(100):
        for player in player_list:

            isDubble = True
            while isDubble:
                i += 1
                move, isDubble = launch_dice()
                player.case += move

                if i > 2:
                    player.case = 10

                plateau[player.case].stop += 1

def launch_dice():
    dice_1 = randint(1,6)
    dice_2 = randint(1,6)

    result = dice_1 + dice_2
    isDubble = dice_1 == dice_2

    return result, isDubble

def show_graph():
    plt.show()
    
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Define the data
    x = []
    y = []
    
    for i in range(len(plateau)):
        x.append(plateau[i].name) 
        y.append(plateau[i].stop)

    # Plot the data
    ax.plot(x, y)
    
    # Add title and labels
    ax.set_title('Simple Line Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    
    # Display the plot
    plt.show()