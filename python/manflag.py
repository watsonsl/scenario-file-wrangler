#! /usr/bin/python -E

import os.path
import stat

curDir = os.getcwd()

def verifyCompletion():
    file1 = False
    renamed_file1 = False
    file2 = False
    copied_file2 = False

    #Check for files
    if not(os.path.exists(curDir + '/file1.txt')):
        file1 = True

    if (os.path.exists(curDir + '/renamed_file1.txt')):
        # If renamed_file1 is present, BOOL flag is set to true
        renamed_file1 = True

    if (os.path.exists(curDir + '/file2.txt')):
        # If file2 still exists, BOOL flag set to true
        file2 = True

    if (os.path.exists(curDir + '/copied_file2.txt')):
        # If renamed_file2 exists, BOOL flag set to true
        copied_file2 = True

    return file1 + renamed_file1 + file2 + copied_file2

# Check for files
if verifyCompletion() == 4: 
    codeDir = curDir.replace('manipulate', 'codes')
    filepath = codeDir + '/manipulate.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            print line.strip()
            line = fp.readline()

else:
    print "Not quite. Re-read the instructions. You should have renamed_file1.txt, file2.txt and copied_file2.txt in the directory."
