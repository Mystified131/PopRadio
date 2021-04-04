#This code imports the necessary modules

import os
import re
import collections
import operator

#This code scans the directory for particular files to delete
 
for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\PopRadio\\Audio'):
    for file in files:
        filepath = subdir + os.sep + file

        #This code works within the scan loop to immediately delete the files

        if (filepath.endswith(".wav")) or (filepath.endswith(".sfk")):
            os. remove(filepath) 

#Here is an exit message throught the console

print("")

print("The designated files have been removed. Thank you.")

print("")