########################################
# Filename: DeleteCompileFiles
# Usage:   python DeleteCompileFiles.py <Directory> > output.txt
########################################

import sys
import os
import fnmatch

#credit: Robin Parmar: http://code.activestate.com/recipes/527746-line-of-code-counter/
def Walk(root='.', recurse=True, pattern='*'):
    """
        Generator for walking a directory tree.
        Starts at specified root folder, returning files
        that match our pattern. Optionally will also
        recurse through sub-folders.
    """
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)
        if not recurse:
            break
                
def DoForEachFileInDirectory(root='', recurse=True, patterns = ["*.*"]):
    # ex. patterns = ["*.class", ]
    for pattern in patterns:
        for fspec in Walk(root, recurse, pattern):
            Execute_Command(fspec)

def Execute_Command(fspec):
    currentSize= os.path.getsize(fspec)
    # total_size += currentSize 
    print "Deleting file: " + str(fspec) + ", size= " +str(currentSize)
    
    # Sample DOS Command from Python:
    # put file in quotes for command so filenames with spaces don't mess it up
    command = "del /q \"" + fspec + "\""
    os.system(command)       
          
def main():

    #TODO:
    # total_size=0
    
    dirName=sys.argv[1]
    numberOfArguments=len(sys.argv)
    if numberOfArguments < 2:
        print("directory name expected. Usage: python ExecuteCommandDir.py <Directory Name>") 
        sys.exit()
    
    # *.sdf *.suo *.user *.tlog *.ali *.o *.pch *.obj *.sbr
    # *.bsc *.map *.pdb *.ilk *.idb *.ncb *.opt *.aps *.plg
    # *.tlh *.tli *.pdb *.idb *.class *.vshost.exe
    patternsToMatch = [ "*.sdf", "*.suo", "*.user", "*.tlog", "*.ali", "*.o", "*.pch", "*.obj", "*.sbr",
                        "*.bsc", "*.map *.pdb", "*.ilk", "*.idb", "*.ncb", "*.opt", "*.aps", "*.plg",
                        "*.tlh", "*.tli", "*.pdb", "*.idb", "*.class", "*.vshost.exe" ]

    DoForEachFileInDirectory(dirName, True, patternsToMatch)

    # print "Total size deleted: " + str(total_size)
            
if __name__ == '__main__':
    main()

