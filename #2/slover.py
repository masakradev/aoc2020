# Slover 2 chellenge 

_input = open('input.txt', 'r').readlines()

counter = 0

for x in _input:
    pattern, data =  x.split(':')
    contain_len, letter = pattern.split(' ')
    c_len_1, c_len_2  = contain_len.split('-')

    char_counter = 0
    for char in data:
        if char == letter:
            char_counter += 1
    
    if int(c_len_1) <= char_counter <= int(c_len_2):
        counter += 1

print(counter)
