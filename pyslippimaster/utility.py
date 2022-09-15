import os
import sys

from pyslippimaster import slippi
from slippi import Game
from slippi import id

sys.path.append("")

# Get the list of all files and directories
path_slippi_main = "/Users/2saint/Desktop/Slippi Files"
slippi_list = os.listdir(path_slippi_main)


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def get_data(file):

    date = Game(file).metadata.date
    stage_played = slippi.id.Stage

    player1 = Game(file).metadata.players[0]
    player2 = Game(file).metadata.players[1]

    player1_str = str(player1)
    player2_str = str(player2)

    p1s = find_nth(player1_str, ":", 1)
    p1e = find_nth(player1_str, ":", 2)

    p2s = find_nth(player2_str, ":", 1)
    p2e = find_nth(player2_str, ":", 2)

    player1_char = player1_str[p1s+1:p1e]
    player2_char = player2_str[p2s+1:p2e]

    p1ns = find_nth(player1_str, "e=", 2)
    p1ne = find_nth(player1_str, ")", 1)

    p2ns = find_nth(player2_str, "e=", 2)
    p2ne = find_nth(player2_str, ")", 1)

    player1_name = player1_str[p1ns+2:p1ne]
    player2_name = player2_str[p2ns+2:p2ne]

    player1_code = ''
    player2_code = ''

    data_tags = {
      'Player_1_Name': player1_name,
      'Player_2_Name': player2_name,
      'Player_1_Character': player1_char,
      'Player_2_Character': player2_char,
      'Date': date
    }

    return data_tags

    # print(date,netplay_code,netplay_name,stage_played,player1,player2,player1_char,player2_char)
    # print("TESTING")
    # print(date, stage_played, player1, player2,)
    # print("---------------date------------------")
    # print(type(date))
    # print(date)
    # print("---------------stage------------------")
    # print(type(stage_played))
    # print(stage_played)
    # print("-----------------Player 1---------------")
    # print(player1)
    # print(type(player2))
    # print("----------------Player 2-----------------")
    # print(player2)
    # print(type(player2))
    # print("----------------Player 1 Character-----------------")
    # print(player1_char)
    # print("----------------Player 2 Character-----------------")
    # print(player2_char)
    # print("----------------Player 1 Name-----------------")
    # print(player1_name)
    # print("----------------Player 2 Name-----------------")
    # print(player2_name)
    # print("-------------------End---------------")


def search_name(p1):
    # get/use the user's input of what they wanted find specifically
    folder_list = []
    for i in range(len(slippi_list)):
        file_name = slippi_list[i]
        new_path = os.path.join(path_slippi_main, file_name)
        fp = "" + new_path
        if p1 == get_data(fp).get("Player_1_Name"):
            folder_list.append(fp)
        elif p1 == get_data(fp).get("Player_2_Name"):
            folder_list.append(fp)

    return folder_list



def set_filename():
    # make a duplicate of an existing file
    old_file = get_file()

    if os.path.exists("guru99.txt"):
        # get the path to the file in the current directory
        src = os.path.realpath("guru99.txt")

        # rename the original file
        os.rename('guru99.txt', 'career.guru99.txt')


def make_folder():
    # Directory to be made
    # TODO Make this based on the user input

    # mode
    mode = 0o666

    directory = "curated"

    # Parent Directory path
    parent_dir = "/Users/2saint/Desktop/"

    # Path
    path = os.path.join(parent_dir, directory)

    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory '% s' created" % directory)


if __name__ == '__main__':
    file = "/Users/2saint/Desktop/Slippi Files/Game_20211215T180925.slp"
    # print(make_folder())
    #print(slippi_list[1])
    #print(get_data(file).get("Player_1_Name"))
    print(search_name("EddyMexico"))
