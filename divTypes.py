import glob

for i in glob.glob("_material_before_act_one/*_before_act_one.xml"):
	f = open(i)
	print(f.readline())
	f.close()