#!/usr/bin/env python3
import os
import re
import sys
from apkleaks.colors import color as col

class util:
	@staticmethod
	def write(message, color):
		sys.stdout.write("%s%s%s" % (color, message, col.ENDC))

	@staticmethod
	def writeln(message, color):
		util.write(message + "\n", color)

	@staticmethod
	def finder(pattern, path):
		matcher = re.compile(pattern)
		found = []
		for fp, _, files in os.walk(path):
			for fn in files:
				filepath = os.path.join(fp, fn)
				with open(filepath) as handle:
					try:
						for line in handle.readlines():
							mo = matcher.search(line)
							if mo:
								found.append(mo.group())
					except Exception:
						pass
		return sorted(list(set(found)))

	@staticmethod
	def check_assets(path):
		
		found = []
		for fp, _, files in os.walk(path):
			for fn in files:
				filepath = os.path.join(fp, fn)
				if '/resources/assets' in filepath and filepath.endswith('.json'):
							found.append(filepath)

		return sorted(list(set(found)))