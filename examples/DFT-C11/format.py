import re

with open('golfed_format_origin.c') as f:
    contents = f.read()

with open('template.txt') as f:
    format_data = f.read()

len_format = len(re.sub('[\n \t]', '', format_data))

if len(contents) < len_format - 5:
    contents += '/*' + '#' * (len_format - len(contents) - 4) + '*/'

with open('golfed_wave_formatted.c', 'w') as f:
    idx = 0
    for char in format_data:
        if char in '\n\t\r ':
            f.write(char)
        else:
            f.write(contents[idx])
            idx += 1
