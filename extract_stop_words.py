# coding=utf-8

import os
import chardet

sw = set()
dir = 'stop_words'
for fn in os.listdir(dir):
    fp = dir +'/'+fn
    print fn
    encoding = chardet.detect(open(fp, 'rb').read(100000000))['encoding']
    print encoding
    for line in open(fp):
        line = line.decode(encoding).strip()
        print fn,'   ', line
        if line:
            sw.add(line)

print len(sw)
f = open('stop_words_pu.txt','w')
for w in sw:
    f.write(w.encode('utf-8')+'\n')
f.close()