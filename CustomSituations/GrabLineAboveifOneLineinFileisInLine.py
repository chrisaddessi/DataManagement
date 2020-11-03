startfilemain = "Devices20200920_ref1.txt"
startfilewordlist = "NewMACs.txt"
outfile = "UPDATED_hosts.txt"
import linecache
num = 0
sfwl = open(startfilewordlist, 'r+')
for testline in sfwl:
	splitted_string = testline.split(',')
	for i in splitted_string:
		strnum = str(num)
		test = splitted_string[num]
		print(test)
		num = num +1
		print(type(splitted_string))
#sfwla = [line for line in sfwl.readlines()]

#test = sfwla[1]
#print(test)

with open(startfilemain) as sfm, open(outfile, "w+") as of:
	for line_no, line in enumerate(sfm):
		#print('ok')
		if 'MAC Address' in line:
			#print('found line with MAC')
			if any(mac in line for mac in splitted_string):
				print('detected')
				linenumber = int(line_no)
				of.write((linecache.getline(startfilemain,linenumber)))
				of.write(line)
