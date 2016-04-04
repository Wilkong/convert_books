#!/usr/bin/python3
from subprocess import call
import sys, os
def main():
	for (dir, _, files) in os.walk(sys.argv[1]):
		for f in files:
			path = os.path.join(dir, f)
			print("Found", f)
			splitted = f.split(".")
			if len(splitted) > 1 and splitted[-1] == "fb2":
				print("Converting", f)
				splitted[-1] = "epub"
				target = os.path.join(dir, ".".join(splitted))
				call(["ebook-convert",path,target])
				os.remove(path)				

if __name__ == "__main__":
    main()
