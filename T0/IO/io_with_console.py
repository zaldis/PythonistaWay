from pprint import pprint

t = input()

data = []
for _ in range(int(t)):
    n = input()
    line = input()
    words = line.split()
    data.append(words)


print('Считанные данные')
pprint(data)
