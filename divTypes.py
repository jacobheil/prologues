'''
import glob

for i in glob.glob("_material_before_act_one/*_before_act_one.xml"):
	f = open(i)

	print(f.readline())
	f.close()
	'''
import codecs, re, glob, csv



for i in glob.glob('_material_before_act_one/*_before_act_one.xml'):
	file_name = i.split("/")[-1][:-19]
	'''
	I use this part to test my script to make sure I was grapping the filenames and to see how many there were. I leave it commented in here just because. you need 'count = 0' somewhere too.
	
	print file_name	
	count = count + 1
print count

	'''
	with codecs.open(i, "r", "utf-8") as opening:
		count = 0
		for line in opening:
			count =  count + 1
	test = [file_name, count]
	print(test)
	

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
