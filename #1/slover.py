# 1 challenge slover

_input = open('input.txt', 'r').read()

entrys = _input.split()

for x in entrys:
    for y in entrys:
        if (int(x)+int(y)) == 2020:
            print(f"Entries {x} {y}")
            print(int(x)*int(y))
