import os
import shutil

newProdFolderOut = open('Results-New Production File.txt', 'w')
newProdFolderOut.write("New Production Specs Folder Created. Stand alone files from dub directory moved to this new folder. Please review. \n")
subFoldersOut = open('Results-subFolders Exist.txt', 'w')
subFoldersOut.write("Sub Folders found in renamed Production Specs folder, Please review. \n")
prodFolderExists = open('Results-Already Existing Production Specs Folder.txt', 'w')
prodFolderExists.write("Production Specs Folder Already Existed, no work needed. \n")
currentRenamed = open('Results-Current Renamed to Production.txt', 'w')
currentRenamed.write("Current folder renamed to Production Specs. \n")
multiCurrentFolders = open('Results-Multiple Current Folders.txt', 'w')

def walkLevel():
    for  dirName in os.walk('.').next()[1]:
	#Check if Production Specs Folder Exists.
        if not os.path.exists(os.path.join(dirName,'./Production Specs')):
	    #loop through folders within dirName and find anything that starts with current. Rename if found.
	    for folderName in os.walk(dirName).next()[1]:
		if folderName.lower().startswith('current'):
		    if not os.path.exists(os.path.join(dirName,'./Production Specs')):
			path = './' + folderName
			os.rename(os.path.join(dirName,path),os.path.join(dirName,'./Production Specs'))
			currentDir = os.path.join(dirName,'./Production Specs')
			currentRenamed.write("Hub Name: " + dirName + " - Previously existing folder : " + path + " Renamed to Production Specs. \n")
		    
			#print out report for sub fodlers that exist in a production spec folder.
			for subDir in os.walk(currentDir).next()[1]:
			    subFoldersOut.write("Directory: " + dirName + " Sub Folder: " +  subDir + "\n")
		    else:
			multiCurrentFolders.write(dirName + " has multiple folders that contain 'current', please review. \n")
			
			
	    #if after looping there is still not a Production Spec folder, create empty folder.
	    if not os.path.exists(os.path.join(dirName,'./Production Specs')):
		os.makedirs(os.path.join(dirName,'./Production Specs'))
		destDir = os.path.join(dirName,'./Production Specs')
		newProdFolderOut.write('Hub Name: %s' % dirName + "\n")
		#this might be helpful, but might also cause a lot of confusion.
		for file in os.listdir(dirName):
		    srcfile = os.path.join(dirName, file)
		    dstfile = os.path.join(destDir, file)
		    
		    if os.path.isdir(srcfile):
			print("ignore the dirs" + srcfile)
		    elif srcfile.lower().endswith(('.pdf', '.doc', '.docx', '.xls', 'xlsx')):
			shutil.move(srcfile, dstfile)
			newProdFolderOut.write(srcfile + " moved from root dir to new prod spec folder \n")
	#if Production Spec Folder already exists, print out report. 
	else:
	    prodFolderExists.write('Hub Name: %s' % dirName + "\n")
		
    newProdFolderOut.close()
    subFoldersOut.close()
    prodFolderExists.close()
    currentRenamed.close()
    multiCurrentFolders.close()
    
walkLevel()
