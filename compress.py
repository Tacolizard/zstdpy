from sys import argv
from zstd import *

inpath = argv[1] #create file object
outpath = argv[1] + '.zstd'

cctx = ZstdCompressor(level=10) #create compressor, using arg for comp level
with open(inpath, 'rb') as ifh, open(outpath, 'wb') as ofh:
	cctx.copy_stream(ifh, ofh)
	