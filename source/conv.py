import csv,sys
topicsfile = sys.argv[1]
outfile = sys.argv[2]
with open(outfile,'w') as o:
    with open(topicsfile) as f:
        rd = csv.reader(f)
        next(rd)
        i = 1
        for line in rd:
            o.write('{},`{} <{}>`_,{}\n'.format(i,line[0],line[3].strip(),line[4]))
            i = i + 1
