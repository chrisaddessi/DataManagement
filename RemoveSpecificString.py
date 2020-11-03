infile = "PotentialTargets.txt"
outfile = "PotentialTargetsMACs.txt"

delete_list = ["MAC Address: "]
with open(infile) as sf, open(outfile, "w+") as of:
    for line in sf:
        for word in delete_list:
            line = line.replace(word, "")
        of.write(line)