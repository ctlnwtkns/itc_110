'''
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.
'''


#locates any gaps in the numbering

#rename all the later files to close this gap


import shutil, os, re

#finds all files with a given prefix in a single folder
# Create a regex that matches part of filename to be substituted
namePattern = re.complile(r'^\d\(d)?.-.*?')

#TODO: Loop over the files in the working directory.
for filename in os.listdir('/Users/caitlin/Documents/school/itc_110/abs_hw/ch9/waiteSmith/majorArcana'):
    mo = namePattern.search(filename)

#TODO: Skip files without a date.
    if mo != None:
        print(filename)
'''
#TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

#TODO: Form the European-style filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterpart

#TODO: Get the full, absolute file paths.
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)


#TODO: Rename the files.
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
#shutil.move(amerFilename, euroFilename) #uncomment after testing


for filename in os.listdir('/home/caitlin/web/waiteSmith/majorArcana2'):
	nameRegex = re.compile(r'dd.-.')	
	mo = nameRegex.search(filename)
	shutil.copy(filename, nameRegex.sub('', filename))
'''	