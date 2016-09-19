import random
import urllib.request

if __name__ == '__main__':
	try:
		numPeeps = int(input("Enter number of peeps ==> "))
	except ValueError:
		print("ERROR: Not a valid int")
		exit(0)

	maleFirstNamesDoc = urllib.request.urlopen('http://www2.census.gov/topics/genealogy/1990surnames/dist.male.first')
	femaleFirstNamesDoc = urllib.request.urlopen('http://www2.census.gov/topics/genealogy/1990surnames/dist.female.first')
	maleFirst = []
	femaleFirst = []
	letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for nameByte in maleFirstNamesDoc:
		tmpstr = nameByte.decode('utf8')
		tmparr = tmpstr.split(' ')
		name = tmparr[0][0] + tmparr[0][1:].lower()
		maleFirst.append(name)
	for nameByte in femaleFirstNamesDoc:
		tmpstr = nameByte.decode('utf8')
		tmparr = tmpstr.split(' ')
		name = tmparr[0][0] + tmparr[0][1:].lower()
		femaleFirst.append(name)

	for i in range(0,numPeeps):
		peep_type = random.choice(['Adult', 'Teenage', 'Child'])
		peep_subtype = random.choice(['Male', 'Female'])
		code = peep_type[0] + peep_subtype[0]
		if peep_subtype == 'Male':
			peep_name = random.choice(maleFirst) + ' ' + random.choice(letters)
		else:
			peep_name = random.choice(femaleFirst) + ' ' + random.choice(letters)
		peep_head = code + '0' + str(random.randint(1,6)) + '_HEAD'
		peep_body = code + '0' + str(random.randint(1,6)) + '_BODY'
		peep_legs = code + '0' + str(random.randint(1,6)) + '_LEGS'
		peep_swim_bod = code + '01_SWIMSUITBODY'
		peep_swim_legs = code + '01_SWIMSUITLEGS'
		peep_skin = 'Palette Skin ' + str(random.randint(1,16))
		peep_upper_cloth = 'Palette UpperClothing ' + str(random.randint(1,16))
		peep_lower_cloth = 'Palette LowerClothing ' + str(random.randint(1,16))
		peep_upper_swim_cloth = 'Palette UpperSwimsuit ' + str(random.randint(1,16))
		peep_lower_swim_cloth = 'Palette LowerSwimsuit '  + str(random.randint(1,16))
		peep_intensity = 'RideIntensity ' + str(random.randint(0,3))
		output = 'Version0 \n'+'Member "' + peep_name + '"\n{\n'+'Type ' + peep_type + '\n'+'SubType ' + peep_subtype + '\n' +'Part Head "' + peep_head + '" 0\n' +'Part Body "' + peep_body + '" 0\n' + 'Part Legs "' + peep_legs + '" 0\n' +'Part SwimSuitBody "' + peep_swim_bod + '" 0\n' +'Part SwimSuitLegs "' + peep_swim_legs + '" 0\n'+peep_skin + '\n' + peep_upper_cloth + '\n' + peep_lower_cloth + '\n' +peep_upper_swim_cloth + '\n' + peep_lower_swim_cloth + '\n' + peep_intensity + '\n' +'}\nLeader 0'
		fName = 'CustomPeep' + str(i) + '.txt'
		out_file = open(fName, 'w')
		out_file.write(output)
		out_file.close()
	print('Peeps Generated')

