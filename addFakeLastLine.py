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


##########################
##### MAIN FUNCTIONS #####
##########################

def addFakeLastLine():
	with open(sys.argv[1]) as f:
		for line in f:
			splitLine = line.strip().split()
			if not splitLine[0].startswith('#'):
				mySamples = len(splitLine)-9
	myOutString = 'Ref\t31\tA31T\tA\tT\t.\t.\tAC=0;AN='+str(1+mySamples)+'\tGT'
	for s in range(0,mySamples):
		myOutString += '\t0'
	myOutString += '\n'
	open(sys.argv[1],'a').write(myOutString)


##########################
#### HELPER FUNCTIONS ####
##########################

def main():
    addFakeLastLine()

if __name__ == "__main__":
    """
    Calls main when program is run by user.
    """
    main();
    raise SystemExit