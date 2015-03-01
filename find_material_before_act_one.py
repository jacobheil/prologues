import glob, codecs, os, time
from bs4 import BeautifulSoup

'''let's assume we'll run the script from a folder that contains a series of subfolders, each of which is named for a work in the EEBO-TCP 1 Corpus. Inside each of those subfolders we'll find a single xml file with a matching name:


folder_this_script_is_in
        |
	|---A00002
	|     |------A00002.xml
	|
	|---A00005
	.     |------A00005.xml
	.
	.
	|
	|---B31385
          |------B31385.xml

Let's loop over these subfolders and find only those xml files that are in Martin Mueller's list:'''

#this function says: check to see if there's a folder within "folder_this_script_is_in" named "material_before_act_one". If such a folder does not exist, create it
if not os.path.exists("_material_before_act_one"):
    os.makedirs("_material_before_act_one")

#this line says: look in the current directory ("folder_this_script_is_in") and find the file "martin-tcp.txt". Open that file in read mode (rather than write mode ["w"], which would erase the file), and assume the character set for the file is utf-8. Refer to this file henceforth as "f"
with codecs.open("martin_list.txt","r","utf-8") as f:
	
	#now read the contents of that file, then remove the "\r" character (it's invisible, but it is there), then split the file each time you hit a carriage return (newline). If we use "print martin_list" after this line, we'll see that martin_list is a list whose members are the files Martin has identified as dramatic works
	martin_list = f.read().replace("\r","").split("\n")

	#let's uncomment the following line and print martin's list so we can see what's in there
	print martin_list
	
	#now let's open each of the xml files in the subdirectories below the present directory if those files are in Martin's list
	for i in glob.glob("*/*.xml"):
		#now if we print i, we see that each i contains the full path to the file (e.g. A00456\\A00456.xml). First let's take only what follows the "\\" character. (NB: On Macs, you'll have to replace "\" with "/".) Then, since martin's list only lists the filename without extension (e.g. A00456 rather than A00456.xml), we'll take a slice of the filenames and ignore the last four characters (the ".xml" characters of the filename) 

		file_name = i.split("/")[-1][:-4]
		
		if file_name in martin_list:
			
			#now let's uncomment the line below and print all of the paths to the files that are in martin_list
			print i
			
			#now open the current i
			with codecs.open(i,"r","utf-8") as play:
				play = play.read()
				
				#now we want to check to see if this play has an act one marker. If it does, we're going to grab all content before that marker and save it to a new file
				if '<div n="1" type="act">' in play:
				
					#wrap the next few lines of code in a try/except wrapper, which basically means: Try to do these things, but if something goes wrong, just print an error to the console, rather than halting
					try:
					
						#transform the xml into a BeautifulSoup object so we can parse the xml easily
						soup = BeautifulSoup(play)
				
						#remove tei_headers from the play (both tagsets seem to have been used)
						[tei_header.extract() for tei_header in soup.findAll("teiHeader")]
						[tei_header.extract() for tei_header in soup.findAll("teiheader")]
						
						#if the play *does* have an act one marker, then let's grab everything before the <div n="1" type="act"> tag and write that little chunk to disk
					
						#then let's write all of the content leading up to act one to disk	
						with codecs.open("_material_before_act_one/" + file_name + "_before_act_one.xml","w","utf-8") as out:
							out.write(unicode(soup).split('<div n="1" type="act">')[0])

					#if something goes wrong, print the error and the name of the file that caused the error
					except Exception as exc:
						print exc, i