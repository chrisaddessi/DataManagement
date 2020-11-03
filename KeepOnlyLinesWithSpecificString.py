good_words = ['Chongqing', 'Aruba', 'Icann', 'Palo','Luxshare', 'Espressif', 'Belkin', 'Hui', 'Mega' , 'Sonim', 'Netgear', 'Liteon', 'Cloud', 'Fn-link', 'Universal' ]



with open('Devices.txt') as oldfile, open('PotentialTargets.txt', 'w') as newfile:
    for line in oldfile:
        if any(good_word in line for good_word in good_words):
            newfile.write(line)