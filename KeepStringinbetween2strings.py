import os
import pyautogui
from multiprocessing import Process
import sys
import time
import re

sf = open("test.txt")
of = open("poopsie.txt", "w+")
good_words = ["Affected Software/OS:\\n"] 

def gettotalnumberofcharinstring(string):
	#string.index('\n')# the number of total characters in line
	if any(good_word in line for good_word in good_words)
		small = string.index(good_words[0])# grabs the start of the affected os
		big = string.index('Vulnerability Detection Method:\n') #grabs the end of affeccted os 
		totaltograb = big - small # total of characters to copy
		for i in totaltograb:
			print("Grabbing the Affected Software/OS:")
			getfullasos = small+i
			fullasos = string[getfullasos]
			of.write(fullasos)


for line in sf:
	gettotalnumberofcharinstring(line)
