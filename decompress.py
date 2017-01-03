from sys import argv
from zstd import *

inpath = argv[1] #create file object

psplit = argv[1].split('.')
pindex = psplit.index('zstd')
psplit.pop(pindex)
outpath = psplit[0] + '.' + psplit[1]


dctx = ZstdDecompressor()
with open(inpath, 'rb') as ifh, open(outpath, 'wb') as ofh:
    dctx.copy_stream(ifh, ofh)
	