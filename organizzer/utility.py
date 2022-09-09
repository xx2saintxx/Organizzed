import os

# Get the list of all files and directories
path_slippi_main = "/Users/2saint/Desktop/Slippi Files"
slippi_list = os.listdir(path_slippi_main)

def make_folder():
    # Directory to be made
    # TODO Make this based on the user input

    # mode
    mode = 0o666

    directory = "PlaceHolder"

    # Parent Directory path
    parent_dir = "/Users/2saint/PycharmProjects/"

    # Path
    path = os.path.join(parent_dir, directory)

    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory '% s' created" % directory)



def rename_file():

    # make a duplicate of an existing file
    if os.path.exists("guru99.txt"):

        # get the path to the file in the current directory
        src = os.path.realpath("guru99.txt")

        # rename the original file
        os.rename('guru99.txt', 'career.guru99.txt')


if __name__ == '__main__':
    print(make_folder())
    print(slippi_list)

