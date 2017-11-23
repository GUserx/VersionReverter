import os, json
import re
import sys


for root, dirs, files  in os.walk("./"):
	
	libraries = sys.argv[1:]

	for file in files:

		for lib in libraries:

			if file.endswith("{0}.xcconfig".format(lib)):

				f = open(os.path.join(root,file))
			
				filedata = f.read()

				if "SWIFT_VERSION" in filedata:

					filedata = filedata.replace('SWIFT_VERSION = 4.0', 'SWIFT_VERSION = 3.2')

					with open(os.path.join(root,file), 'w') as fi:
						fi.write(filedata)
						print('done')
					
				f.close()