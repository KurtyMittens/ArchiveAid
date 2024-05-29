pop = []
with open('test.pop', "r") as file:
    for i in file:
        pop.append(i.strip())
    file.close()

print(pop)
pop2 = '4569874521'
pop2 = '\n'.join(pop2)

with open('test.pop', 'w') as file2:
    file2.write(pop2)
    file2.close()

pop3 = []
with open('test.pop', "r") as file:
    for i in file:
        pop3.append(i.strip())
    file.close()
print(pop3)