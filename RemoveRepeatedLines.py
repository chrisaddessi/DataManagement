lines = open('rockyou.txt', 'r').readlines()

lines_set = set(lines)

out  = open('Output.txt', 'w')

for line in lines_set:
    out.write(line)