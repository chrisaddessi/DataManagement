startfile = "Targest.txt"
outfile = "MACs.txt"

with open(startfile) as sf, open(outfile, "w+") as of:
	for line in sf:
		
		splitted_string = line.split()
		mac = splitted_string[2]
		print(mac)
		line = mac
		of.write(line + "\n")
		
