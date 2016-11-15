import re

MasksEnumerator = dict()
MasksCounter = dict()

with open('access.log', 'r') as myFile:
	myFileVariable = myFile.read().replace('\n', '')

IPs = list(set(re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', myFileVariable)))

IPs.sort()

for IPIndex in range(len(IPs)):
	currentMask = ''
	dotsCount = 1
	for char in IPs[IPIndex]:
		if dotsCount <= 3:
			if char == '.':
				dotsCount += 1
			currentMask += char	
		
	if IPIndex == 1:
		if currentMask in MasksEnumerator:
			MasksEnumerator[currentMask] += IPs[IPIndex]
			MasksCounter[currentMask] += 1
		else:
			MasksEnumerator[currentMask] = IPs[IPIndex]
			MasksCounter[currentMask] = 1
	else:
		if IPs[IPIndex][:len(currentMask)] == IPs[IPIndex - 1][:len(currentMask)]:
			MasksEnumerator[currentMask] += ' ' + IPs[IPIndex]
			MasksCounter[currentMask] += 1
		else:
			MasksEnumerator[currentMask] = IPs[IPIndex]
			MasksCounter[currentMask] = 1

for key in MasksEnumerator:
	print (key, MasksCounter[key], MasksEnumerator[key])