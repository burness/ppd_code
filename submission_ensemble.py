'''
Coding Just for Fun
Created by burness on 16/3/27.
'''
from collections import defaultdict, Counter
from glob import glob
import sys

glob_files = sys.argv[1]
loc_outfile = sys.argv[2]
print glob(glob_files)

def kaggle_bag(glob_files, loc_outfile, method="average", weights="uniform"):
    if method == "average":
        scores = defaultdict(list)
    with open(loc_outfile,"wb") as outfile:
        # for i, glob_file in enumerate(filter_subs(glob(glob_files))):
        print glob(glob_files)
        for i , glob_file in enumerate(glob(glob_files)):
            print "parsing:", glob_file
            print "i:" , i
            # sort glob_file by first column, ignoring the first line
            lines = open(glob_file).readlines()
            lines = [lines[0]] + sorted(lines[1:])
            for e, line in enumerate( lines ):
                if i == 0 and e == 0:
                    outfile.write(line)
                if e > 0:
                    row = line.strip().split(",")
                    each_score = float(row[1])
                    scores[row[0]].append(each_score)
        print scores
        for j,k in sorted(scores.items(),key=lambda d:d[0]):
            outfile.write("%s,%s\n"%(j,reduce(lambda x, y: x + y, k) / len(k)))
        print("wrote to %s"%loc_outfile)
        # print("wrote to %s"%loc_outfile)


kaggle_bag(glob_files,loc_outfile)