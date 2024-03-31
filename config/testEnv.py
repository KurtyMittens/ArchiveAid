import fileinput

# File = fileinput.input("config/settings.txt")

text = open("config/settings.conf", 'rt')
filepath = []
for i in text:
    if i[0] != '#' and i[0] != '\n' and i[0] != ' ':
        filepath.append(i.split('-'))

print(filepath)
    