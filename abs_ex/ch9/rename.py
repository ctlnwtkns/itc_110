import os, shutil

shutil.copytree('/home/caitlin/web/waiteSmith/majorArcana', '/home/caitlin/web/waiteSmith/majorArcana2')

for filename in os.listdir('/home/caitlin/web/waiteSmith/majorArcana2'):
	nameRegex = re.compile(r'dd.-.')	
	mo = nameRegex.search(filename)
	shutil.copy(filename, nameRegex.sub('', filename))
	