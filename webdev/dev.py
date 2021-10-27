from os import mkdir, chdir, path, system
from dataclasses import dataclass
from sys import argv
from time import sleep
"""
a module to generate the boiler plate for the web developement projects.
author: Moody0101
structure:
	dev class:
		execute() (hands data from argv) ==>  init() (generates everything)
"""
def createfile(name, content):
	with open(name, 'w+') as file:
		file.write(content)
		return 0
	return 1

def generathtml(css, js, docname):
	html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="{css}.css">
	<script type="text/javascript" src="{js}.js" defer></script>
	<title>{docname}</title>
</head>
<body>
	
</body>
</html>
	"""
	return html

@dataclass
class dev:
	"""
	even if nothing was specified, everything will be generated.
	"""
	projectName: str
	html: str = "index.html"
	css: str = "style.css"
	js: str = "script.js"
	scss: str = None
	data: str = "data"
	pages: str = "pages"
	signature = "\\*made with dev*\\"
	@property
	def generate(self):
		"""
		generating an html file that makes sense to what the user have specified in the cmd.
		using another func above and called by the init.	
		"""
		return generathtml(self.css, self.js, self.docname)
	def init(self):

		"""
		an initializer that makes the dirs and files.
		"""
		
		if not path.exists(self.projectName):
				print(f"Making dir: {self.projectName}")
				sleep(0.5)
				mkdir(self.projectName)
				chdir(self.projectName)
				self.commit()
		else:
				chdir(self.projectName)
		    	self.commit()
	def commit(self):
			print(f"Making dir: {self.data}")
			sleep(0.5)
			mkdir(self.data)
			print(f"Making file: {self.html}")
		    sleep(0.5)
			createfile(self.html, self.generate)
			print(f"Making dir: css")
		    sleep(0.5)
			mkdir("css")
			print(f"Making file: css/{self.css}")
		    sleep(0.5)
			createfile(f"ccs/{self.css}", self.signature)
			print(f"Making dir: js")	
		    sleep(0.5)
			mkdir("js")
			print(f"Making file: js/{self.js}")
		    sleep(0.5)
			createfile(f"js/{self.js}", self.signature)

	def execute(self):
		"""
		this function is the function that collects everything from the command line
		to execute the commands respecting what he user  want.
		uses len(sys.argv) to make sure that everything is in place
		"""
		self.projectName = argv[1]
		self.init()

def main():
	command = dev()
	dev.execute()

if __name__ == '__main__':
	main()
