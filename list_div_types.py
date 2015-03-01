import glob,codecs, os, time
from bs4 import BeautifulSoup

#I know I'm probably making this too complicated by using glob, but my goal is to use the list of filenames like we used Martin's list. I'll also want to print the filename[:19] as part of the csv I'm trying to make here. I probably need the csv module, but my columns will be non-uniform (eg. some could have a "prologue," some "prologue" and "intro," and some will have nothing at all).

for name in glob.glob('*'):
	print name

	with codecs.open(name,"r","utf-8") as opening:
		opening = opening.read()

		#so I think I can get as far as reading the file -- the play opening -- using codecs, but i get stuck here. I want to look for a string matching '<div type=' and, if it exists in the file, grab that type ("prologue" or "dedication" or "introduction" etc, whatever is between the double quotes) and store it. But no, if there are multiple, it'll overwrite the variable each time. So I could make the variables iterative (var + 1 each time there's a new div type). Or I could write it somewhere else for holding? 

		#Ugh I'm giving up for the day. What I want to do is grab "name" which should be the TCP number, and concatenate that with each "<div type="" found in a comma separated row. (cf. line 22-23). Then append that row to a file, which I'm calling "div_type.txt".

		for types in opening


		for '<div type=' in opening:
			div_type = 


			with open("div_type.txt", "a") as myfile:
			    myfile.write(name + ", " div_type)

			    myfile.close() 

	#with codecs.open(name,"w","utf-8") as out:
	#	out.write(unicode(soup).split('<div n="1" type="act">')[0])