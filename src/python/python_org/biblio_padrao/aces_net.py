from urllib.request import urlopen

with urlopen('http://docs.python.org/3/') as response:
    for line in response:
        line = line.decode()
        if 'update' in line:
            print(line.rstrip())
