'''
Created on Feb 18, 2016

@author: ecary

Called with:

python random_line_gen.py 1 - <input_file_src> 2 - <input_file_trgt> 3 - <num_line_wanted> 4 - <output_file_src> 5 - <output_file_trgt> 6 - <updated_file_name_source> 7 - <updated file_name_target
will then output new version of original having deleted chosen lines

Maybe later rewrite this with options - command line arguments are little unwieldy
'''

import sys
import random
import itertools

res = open('res.txt','w')
output_source = open(sys.argv[4],'w')
output_target = open(sys.argv[5],'w')

#Combine source and target files into one file (line by line, separated by "**********"
with open(sys.argv[1]) as source, open(sys.argv[2]) as trgt:
    for line1, line2 in zip(source, trgt):
        res.write("{}**********{}\n".format(line1.rstrip(),line2.rstrip()))
        #print("{}*********{}".format(line1.rstrip(\n), line2.rstrip()))
res.close()

with open("res.txt") as res:
    all_lines = res.readlines()
    lines = random.sample(all_lines, int(sys.argv[3]))
    #store used lines to delete later
    source_rm = set()
    #write each line to new file
    for line in lines:
        twoSent = line.split("**********")
        output_source.write(twoSent[0].strip() + "\n")
        source_rm.add(twoSent[0].strip())
        
        output_target.write(twoSent[1].strip() + "\n")

alt_source = open(sys.argv[6],'w')
alt_target = open(sys.argv[7],'w')
#Find lines in original, only write non-used lines to new files
with open(sys.argv[1]) as source, open(sys.argv[2]) as trgt:
    for line1, line2 in zip(source, trgt):
        if line1.strip() not in source_rm:
            alt_source.write(line1.strip() + "\n")
            alt_target.write(line2.strip() + "\n")