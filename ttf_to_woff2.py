from fontTools.ttLib.woff2 import compress as woff2_compress
from pathlib import Path
inputfile = Path(input("Input file: ").replace('"',''))
print(inputfile)
outputfile = inputfile.parents[0] / (inputfile.stem + ".woff2")
woff2_compress(inputfile, outputfile)
print("Done!")