import time
import sys

class Directory:
    def __init__(self):
        self.directory = {}

    def create(self, path):
        # CREATE grains/squash
        folders = path.split('/')
        current_directory = self.directory

        for folder in folders:
            # [grains, squash]
            # if grains, if squash not in current directory, add it
            if folder not in current_directory:
                current_directory[folder] = {}
            current_directory = current_directory[folder]

    def list(self, current_directory=None):
        if current_directory is None:
            current_directory = self.directory
        #go through each nested key and print 
        for key in current_directory.keys():
            print(f'  {key}')
            self.list(current_directory[key])

def process_input(input):
    new_directory = Directory()
    for command in input.splitlines():
        # print(f"command is {command}")
        if command !="":
            command_line = command.split(" ")
            if (len(command_line) > 1):
                # the command is either CREATE, MOVE, DELETE    
                request = command_line[0]
                if request == "CREATE":
                    new_directory.create(command_line[1])
                if request == "LIST":
                    # print(command)
                    new_directory.list()

print("Please enter directory commands (press Ctrl+D to finish):")
input = sys.stdin.read()
process_input(input)

