from pprint import pformat

with open('input.txt', 'r') as f:
    t = f.readline()

    data = []
    for _ in range(int(t)):
        n = f.readline()
        line = f.readline()
        words = line.split()
        data.append(words)


with open('output.txt', 'w') as f:
    f.write(pformat(data))

