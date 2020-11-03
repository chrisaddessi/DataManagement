startfile = input("Enter file to remove blank lines: ")
with open(startfile) as sf, open("RemovedBlankLines.txt", "w+") as of:
	for line in sf:
		if line.strip():
			of.write(line)