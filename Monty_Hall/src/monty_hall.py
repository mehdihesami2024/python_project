import random
from typing import Tuple

def monty_hall(switch_door: bool) -> bool:
    """ Simulate a single Monty Hall game

    :param switch: if True, the contestant will switch their choice after a goat door is reaveled.
    :return: True if the contestant won car, False otherwise
    """

    doors = ["goat", "goat", "car"]
    random.shuffle(doors)

    # contestant select a door initially
    user_choice = random.choice(range(3))
    doors_reaveled = [i for i in range(3) if (i != user_choice) and (doors[i] != "car")]
    door_reaveled = random.choice(doors_reaveled)


    # if contestant decides that switch, the their final choice is the remaining door.
    if switch_door:
        final_choice = [doors[i] for i in range(3) if i != user_choice and i != door_reaveled ][0]

    # the contestant keep the initial choice
    else:
        final_choice = doors[user_choice]

    return final_choice == "car"


def simulate_games(num_of_games: int):
    """simulate a number of games Monty Hall and print the statistics.

    :param num_of_games:number of games to simulate.
    :return: winning percentge by switching and not swithing.
    """
    num_wins_with_switching = sum([monty_hall(True) for i in range(num_of_games)])
    num_wins_without_swithing = sum([monty_hall(False) for i in range(num_of_games)])
    return num_wins_with_switching, num_wins_without_swithing


if __name__ =="__main__":
    num_of_games = 1000
    num_wins_with_switching, num_wins_without_switching = simulate_games(num_of_games)
    print(f'winning percentage with switching doors={num_wins_with_switching/num_of_games*100}')
    print(f'winning percentage  without switching doors= {num_wins_without_switching/num_of_games*100}')



    
    

