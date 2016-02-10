'''
Tolliver, Sumner, Cary
Read and store phrase table alignment data
This reads from toy German file, will need to be reworked
    der ||| the ||| 0.3 ||| ||| 
to deal with the Spanish file (different format there--binarization??? phrasal alignment??)
'''
import sys
tupleList = []

with open(sys.argv[1]) as phrase_table:
    for line in phrase_table:
        tupleList.append((line.split('|||')[0].strip(),line.split('|||')[1].strip(),line.split('|||')[2].strip()))
print tupleList
