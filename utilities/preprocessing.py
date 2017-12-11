import sys
import os
from sets import Set
sys.path.append('../library')
from pre import *
from  pandas import read_csv

def find(dataframe, name):
    for count, sname in enumerate(dataframe['song name']):
        if  sname == name :
            return dataframe['avg frame'][count]


if len(sys.argv) != 3:
    print( 'Usage: python preprocessing.py SONGFODLER PGZFOLDER')
else :
    inPath= sys.argv[1]
    outPath = sys.argv[2]
    csv = read_csv(os.path.join(outPath,'metadata.csv'))
    i =0
    for path,dir,files in os.walk(inPath):
        for f in files:
            if f.endswith('wav'):
                # create preaudio instance and stretch to uniform frame size
                instance  = PreAudio(os.path.join(path,f))
                fTrim = filter(lambda x: not (x.isdigit() or x == '_'), instance.name) # to trim _1, _2, _3... off(number of song seg)_
                avgframe = find(csv, fTrim)
                instance.stretch_seg(avgframe)
                instance.save(outPath)
            print 'progress : ', i+1, ' of ', len(files)
            i +=1
