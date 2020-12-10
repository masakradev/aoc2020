
input_file = open('input.txt', 'r').readlines()

ids = []

for line in input_file:
    interval_a = 0
    interval_b = 127

    interval_c = 0
    interval_d = 7
    
    row = 0
    seat = 0

    for x in line[0:6]:
        if x == "F":
            interval_b = int((interval_b+interval_a)/2)
        elif x == "B":
            interval_a = int((interval_b+interval_a)/2)+1

    if line[6:7] == "F":
        row = interval_a
    else:
        row = interval_b

    for c in line[7:9]:
        if c == "L":
            interval_d = int((interval_d+interval_c)/2)
        elif c == "R":
            interval_c = int((interval_d+interval_c)/2)+1

    if line[9:10] == "R":
        seat = interval_d
    else:
        seat = interval_c

    ids.append((row * 8) + seat)


print(f"Solution: {sorted(ids)[-1]}")