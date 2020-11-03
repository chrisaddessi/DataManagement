#Example
# this is another line
# this is my previous line with some info What Game features a Character With a Pulmber with a Italian name
# this is my line with special string SuperMario
# this is another line  
#OUTPUT
#
# this is my previous line with some info What Game features a Character With a Pulmber with a Italian name
# this is my line with special string SuperMario
#
import linecache

good_words = ['Palo', 'Icann', 'Aruba', 'AzureWave', 'Liteon', 'Technology', 'Belkin', 'Hewlett', 'Raspberry', 'CyberTAN', 'Radiant', 'Mega', 'Netgear' ]



with open('DevicesEdit.txt') as oldfile, open('PotentialTargets.txt', 'w') as newfile:
	for line_no, line in enumerate(oldfile):
		if any(good_word in line for good_word in good_words):
			linenumber = int(line_no)
			newfile.write((linecache.getline('DevicesEdit.txt',linenumber)))
			newfile.write(line)
	#for line in oldfile:

        
		
		#if any(good_word in line for good_word in good_words):
			#newfile.write(line)