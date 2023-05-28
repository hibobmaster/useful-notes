from fontTools.ttLib.woff2 import compress as woff2_compress
inputfile = r"C:\Users\BobMaster\Downloads\LXGWWenKai-Regular.ttf"
outputfile = r"C:\Users\BobMaster\Downloads\LXGWWenKai-Regular.woff2"
woff2_compress(inputfile, outputfile)
print("Done!")