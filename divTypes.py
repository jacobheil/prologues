'''
import glob

for i in glob.glob("_material_before_act_one/*_before_act_one.xml"):
	f = open(i)

	print(f.readline())
	f.close()
	'''
import codecs

with codecs.open('_material_before_act_one/A00725_before_act_one.xml',"r","utf-8") as play:
	play = play.read()
	if '<div type="to_the_reader">' in play:
		print "hooray"


'''
f = open('_material_before_act_one/A00725_before_act_one.xml')
for line in f:
		print line

'''
