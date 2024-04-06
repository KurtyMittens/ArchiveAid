# File = fileinput.input("config/settings.txt")
import os
class Recent:
    def __init__(self):
        self.filesave = []
        with open("config/recent.conf", 'r') as file:
            for i in file:
                if i[0] != '#' and i[0] != '\n' and i[0] != ' ':
                        file = i.strip()
                        self.filesave.append(file.split("-"))

    def get_filepath(self):
         return self.filesave[1:]
    
    def get_sourcepath(self):
         return self.filesave[0]
