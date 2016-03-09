#finds all files with a given prefix in a single folder

#locates any gaps in the numbering

#rename all the later files to close this gap


import shutil, os, re

os.chdir('/Users/caitlin/Documents/school/itc_110/abs_hw/ch9/waiteSmith/majorArcana')

# Create a regex that matches part of filename to be substituted
nameRegex = re.compile(r'^(\d)(\d)?(.-.)(T|W\w*)?(\W)?(\w*.)?(\w*.)?(\w*)(.jpg)')

#TODO: Loop over the files in the working directory.
for filename in os.listdir('.'):
	mo = nameRegex.search(filename)
	if mo != None:
	#TODO: Get the different parts of the filename.
		int1 = mo.group(1) 
		int2 = mo.group(2)
		ext = mo.group(9)
		if int2 != None:
			newfile = nameRegex.sub(int1 + int2 + ext, filename)
		else:
			newfile = nameRegex.sub(int1 + ext, filename)
		#print(newfile)
				
#TODO: Get the full, absolute file paths.
	absWorkingDir = os.path.abspath('.')
	newFilename = os.path.join(absWorkingDir, newfile)

#TODO: Rename the files.
	print('Renaming "%s" to "%s"...' % (filename, newFilename))
	shutil.move(filename, newFilename) #uncomment after testing
