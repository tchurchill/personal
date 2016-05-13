import os
import shutil
outfile = open('BA_Review_Needed.txt', 'w')
outfile.write('Folders Not Updated\n')

def renameSpecs():
    for dirName in os.walk('C:/SPSSpecService/EDI Guidelines').next()[1]:
        if(dirName.startswith("B")):#Since where breaking this up, define alpha character were searching through.
            dirName = "C:/SPSSpecService/EDI Guidelines/" + dirName
            if not os.path.exists(os.path.join(dirName,'./Production Specs')):
                hubToOutput = True
                for newDir in os.walk(dirName).next()[1]:
                    if "Current" in newDir:
                        os.rename(os.path.join(dirName,newDir), os.path.join(dirName,'./Production Specs'))
                        hubToOutput = False
                if hubToOutput:
                    outfile.write(dirName + ", No Current Directory Exists" + '\n')
            else:
                outfile.write(dirName + ", Production Folder Already Exists" + '\n')

if __name__ == "__main__":
    renameSpecs()
