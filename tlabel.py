#!/bin/env python3

###############################################################################
#                                                                             #
#      Usagi Paper tape labeler program                                       #
#                                                                             #
#      V 0.01A : Robsbots : 26-05-26                                          #
#                                                                             #
#      License : PD. Public Domain. Free.                                     #
#                As in Beer!!!! Do what you like like with this code.         #
#                                                                             #
#      Note : argparse has it's own license and is included as a courtesy     #
#             Please see details in included file                             #
#                                                                             #
###############################################################################
#                                                                             #
#     Make file executable                                                    #
#                                                                             #
#  $ chmod +x ./tlabel.py                                                     #
#                                                                             #
###############################################################################
#                                                                             #
#     To use                                                                  #
#                                                                             #
#  $ tlabel.py --label "Hellorld!" -f ./out.bin                               #
#                                                                             #
#  --> Outputs binary file "./out.bin" containing a tape label "HELLORLD!"    #
#                                                                             #
#  $ tlabel.py --label "Hellorld!" -a ./out.txt                               #
#                                                                             #
#  --> Outputs ascii representation to file ./out.txt                         #
#                                                                             #
#  $ tlabel.py --label "Hellorld!" -t                                         #
#                                                                             #
#  --> Outputs text representation to screen                                  #
#                                                                             #
#                                                                             #
#          Any combination of the above ocommands may be used                 #
#                                                                             #
#  $ tlabel.py -h                                                             #
#                                                                             #
#     Shows help screen                                                       #
#                                                                             #
###############################################################################

import argparse
import os

# import 2 character sets: charlookupA and charlookupB
from charset import *

# Set character set
#charset = charlookupA
charset = charlookupB


# Return string of stars/spaces representing 6 bits
def numtostars(num):
	returnString = ""
	for n in [64,32,16,8,4,2]:
		if (num & n):
			returnString = returnString + "*"
		else:
			returnString = returnString + " "
	return returnString


# Instantiate the parser
parser = argparse.ArgumentParser(description='Tape Labeler')

## Add function - Test text output to screen
parser.add_argument('-t', "--test", action="store_true", help='Print output to screen')

## Add function - Label to place on tape
parser.add_argument('-l', "--label", action='store', type=str, help='Label to punch on tape.')

## Add function - Binary file output
parser.add_argument('-f', "--filename", action="store",type=str, help='Binary Output file path')

## Add function - Text file output
parser.add_argument('-a', "--ascii", action="store",type=str, help='Text Output file path')


# Process command line argumants
args = parser.parse_args()

# Create lists to hold byte codes and ascii for title
titleFileData = []
ascFileData = []
# Holds list of numbers to create a single character
code = []

if args.label:											# Was the label provided on the command line ?
	labelString = args.label							#  Yes. Set tape label.
else:															# No.
	labelString = input("Enter tape title :- ")			#  Prompt user and set tape label

# Set title to upper case and step though each letter
for letter in labelString.upper():
	if (letter in charset):								# Look up bytes to build character
		code = charset[letter]							#   Set byte code for character		
	else:												# Character not found
		code = charset["."]								#   Unkown letter. Substitute '.'
	for i in code:										# Loop though each byte in character
		titleFileData.append( i )						#   Add bit pattern to binary file data
		ascFileData.append( numtostars( i ) )			#   Add star pattern to asc file data
	
# If testing print ascii output to screen
if args.test:											# Are we testing ?
	for a in ascFileData:								#   Then for each byte of data
		print(a)										#  	Print it out

# Output tape title data to binary file
if ( args.filename ):
	fileData = bytearray(titleFileData)					#  Crete binary array from datastring
	with open(args.filename, "wb") as bin_file: 		#  Create binary file
		bin_file.write(fileData)						#  Output binary data to file

# Output tape title data to binary file
if ( args.ascii):
	dataString = "\n".join(ascFileData)					#  Create str of binary with line feeds for each byte
	with open(args.ascii, "w") as ascii_file:			#  Create text file
		ascii_file.write(dataString)					#  Output ascii data

