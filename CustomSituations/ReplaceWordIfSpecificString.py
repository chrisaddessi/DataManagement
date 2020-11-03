import os 

iteration = 0
startfile = 'UnknownDevices'
workingfile = 'FixingUnkown'
previteration = 0
while 1 == 1:
	macoui = input('EnterMAC: ')
	currentword = 'Unknown'
	replacewordwithme = input('EnterCompany: ')
	iterationstr = str(iteration)
	previterationstr = str(previteration)
	fullpathtonewestfile = 'FixingUnkown' + iterationstr + '.txt'
	with open ( startfile + previterationstr +'.txt', 'r') as myfile, open('FixingUnkown' + iterationstr + '.txt', 'a') as newfile:
		for myline in myfile:

			if macoui in myline:
				if currentword in myline:
					newfile.write(myline.replace(currentword, replacewordwithme))
			newfile.write(myline)

	os.system(fullpathtonewestfile)
	previteration = iteration
	startfile = workingfile
	iteration = iteration + 1