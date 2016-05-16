import os
import shutil
outfile = open('BA_Review_Needed.txt', 'w')
outfile.write('Folders Not Updated\n')

def renameSpecs():
    for dirName in os.walk('C:/SPSSpecService/EDI Guidelines').next()[1]:
        if(dirName.startswith("W")):#Since where breaking this up, define alpha character were searching through.
            dirName = "C:/SPSSpecService/EDI Guidelines/" + dirName
            if not os.path.exists(os.path.join(dirName,'./Production Specs')):
                noCurrent = True
		subDir = False
                for newDir in os.walk(dirName).next()[1]:
                    if "Current".lower() in newDir.lower():
                        os.rename(os.path.join(dirName,newDir), os.path.join(dirName,'./Production Specs'))
                        noCurrent = False
			newDir = dirName + "/Production Specs"
			for sub in os.walk(newDir).next()[1]:
			    sub = newDir + "/" + sub
			    if(os.path.isdir(sub)):
				subDir = True
                if noCurrent:
		    os.makedirs(os.path.join(dirName,'./Production Specs'))
                    outfile.write(dirName + ", No Current Directory Exists. Please review" + '\n')
		if subDir:
		    outfile.write(dirName + ", Copied Current to Production Specs, Production Specs folder still contains sub Folders. Please review" + '\n')
            else:
                outfile.write(dirName + ", Production Folder Already Exists. No review necessary" + '\n')

if __name__ == "__main__":
    renameSpecs()
