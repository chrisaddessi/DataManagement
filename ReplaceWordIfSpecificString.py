startfile = 'hostsiptemp.txt'
outfile = 'HOSTS_IP.txt'


wordtoreplace = 'Nmap scan report for '
replacewordwithme = ''


with open (startfile, 'r') as sf, open( outfile, 'a') as of:
	for line in sf:
		if wordtoreplace in line:
			of.write(line.replace(wordtoreplace, replacewordwithme))
		
