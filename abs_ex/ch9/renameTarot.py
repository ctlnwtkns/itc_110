import os, shutil

shutil.copy(majorArcana, majorArcana2)

for filename in os.listdir():
	nameRegex = re.compile(r'dd.-.')	
	nameRegex.sub('', filename)
	
