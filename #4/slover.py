

input_file = open('input.txt', 'r').read()
input_data = input_file.split('\n\n')

required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

valid = 0

for passport in input_data:
    temp_data = passport.rstrip()

    fields = []
    for x in temp_data.splitlines():
        for z in x.split(' '):
            fields.append(z.split(':')[0])


    va = True
    for req in required:
        if req not in fields:
            va = False
    
    if va:
        valid += 1
    


print(f"Answer {valid}")