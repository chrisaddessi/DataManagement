bad_words = ['MAC']
startfile = 'UPDATED_hosts.txt'
outfile = 'hostsiptemp.txt'

with open(startfile) as oldfile, open(outfile, 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)