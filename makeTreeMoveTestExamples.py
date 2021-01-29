#!/usr/bin/env python3
# Name: Bryan Thornlow
# Date: 9/4/2018
# getGenomeActivityDist.py

import sys
import os
import time
import random
import numpy as np 
import gzip
import math

"""
Input format:

S1  m1,m2,m3,m4
S2  m1,m2,m3,m5
S3  m1,m2,m6
S4  m7
S5  m1,m2,m3?,m8
S6  m1,m2,m8
S7  m1,m4,m5,m6 
S8  m1,m4,m7

Output format:
- .fasta file with samples 1-4, 5-8
- mutations to genotypes
"""

##########################
##### MAIN FUNCTIONS #####
##########################

def makeTreeMoveTestExamples():
    SEQ_LENGTH = 30
    randomMut = {'A':'CGT','C':'AGT','G':'ACT','T':'ACG'}
    ambiguousNucs = {'A':'RWMDHV','C':'YSMBHV','G':'RSKBDV','T':'YWKBDH'}
    #ambiguousNucs = {'AG':'R','CT':'Y','GC':'S','AT':'W','GT':'K','AC':'M','CGT':'B','AGT':'D','ACT':'H','ACG':'V','ACGT':'N'}

    defaultSeq = ''
    for i in range(0,SEQ_LENGTH):
        defaultSeq += random.choice('ACGT')

    sampleToMuts = {}
    mutToGenotype = {}
    ambiguousMutToGenotype = {}
    with open(str(sys.argv[1])) as f:
        for line in f:
            splitLine = (line.strip()).split()
            muts = splitLine[1].split(',')
            sampleToMuts[splitLine[0]] = muts
            for k in muts:
                if not k.endswith('?'):
                    if not k in mutToGenotype:
                        mutToGenotype[k] = ''
                else:
                    ambiguousMutToGenotype[k] = ''

    myOutGenotypes = ''
    nts = list(np.random.choice(list(range(0,SEQ_LENGTH)), len(mutToGenotype), replace=False))
    #print(nts)
    for i in range(0,len(nts)):
        myGenotype = defaultSeq[nts[i]]+str(nts[i])+random.choice(randomMut[defaultSeq[nts[i]]])
        mutToGenotype[sorted(list(mutToGenotype.keys()))[i]] = myGenotype
        myOutGenotypes += sorted(list(mutToGenotype.keys()))[i]+'\t'+myGenotype+'\n'
    for k in ambiguousMutToGenotype:
        mutToGenotype[k] = mutToGenotype[k[:-1]][:-1]+random.choice(ambiguousNucs[(mutToGenotype[k[:-1]][0])])
        myOutGenotypes += k+'\t'+mutToGenotype[k]+'\n'
    open(sys.argv[1].split('.')[0]+'_genotypes.txt','w').write(myOutGenotypes)

    myOutFa = '>Ref\n'+defaultSeq+'\n'
    for s in range(1,5):
        myOutFa += '>S'+str(s)+'\n'+applyMuts(defaultSeq, sampleToMuts['S'+str(s)], mutToGenotype)+'\n'
    open(sys.argv[1].split('.')[0]+'_1.fa','w').write(myOutFa)

    myOutFa = '>Ref\n'+defaultSeq+'\n'
    for s in range(5,9):
        myOutFa += '>S'+str(s)+'\n'+applyMuts(defaultSeq, sampleToMuts['S'+str(s)], mutToGenotype)+'\n'
    open(sys.argv[1].split('.')[0]+'_2.fa','w').write(myOutFa)


##########################
#### HELPER FUNCTIONS ####
##########################

def applyMuts(seq, muts, mutToGenotype):
    myReturn = list(seq)
    for k in muts:
        g = mutToGenotype[k]
        myReturn[int(g[1:-1])] = str(g[-1])
    return(''.join(myReturn))

def main():
    makeTreeMoveTestExamples()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit



