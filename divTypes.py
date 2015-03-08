import codecs, re, glob, csv
from bs4 import BeautifulSoup


divCounts = {}

'''
divTypes = []
csvFile = csv.writer(open("playID_opening.csv", "w"))
csvFile.writerow(["file_name", "opening"])
'''
for i in glob.glob('_material_before_act_one/*_before_act_one.xml'):
	file_name = i.split("/")[-1][:-19]
	
	opening = open(i, "r")

	for line in opening:
		s = re.match(r'^(<div\stype=")(.*)(">)$', line)

		try:
			divType = s.group(2)
			if divType not in divCounts:
				
				divCounts[divType] = [0]
			
			divCounts[divType][0] += 1

			'''
			count = count + 1
			csvFile.writerow([file_name, divType])    
			'''
		except:
			continue

print divCounts

	

'''
with codecs.open('_material_before_act_one/A00725_before_act_one.xml',"r","utf-8") as play:
	for line in play:
		print line

	play = play.readline()
	print play
for hit in play:
		if 'xmlns' in hit:
			print "hooray"
			count = count + 1
			print count
'''
	


'''
f = open('_material_before_act_one/A00725_before_act_one.xml')
for line in f:
		print line

'''
