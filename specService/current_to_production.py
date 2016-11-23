import os
import shutil
renamedFolders = open('Renamed.txt','w')
renamedFolders.write('Renamed Folders' + '\n')
denied = open('Rename_fail.txt', 'w')
denied.write('Rename Failed' + '\n')
noCurrentFolder = open('No_Current_Exists.txt', 'w')
noCurrentFolder.write('No Current Folder Existed' + '\n')
subFolders = open('Subfolders_in_Prod_spec_folder.txt', 'w')
subFolders.write('SubFolders Exist, Please review' + '\n')
noWork = open('Prod_Spec_Already_Exists.txt', 'w')
noWork.write("Prod folder already existed" + '\n')
double = open('Prod_and_Current_Exist.txt', 'w')
double.write('Current and Poduction Spec folders both exist...bad' + '\n')

def renameSpecs():
    ### B:/Hub EDI Guidelines
    for dirName in os.walk('C:/specService/Hub EDI Guidelines').next()[1]:
        if(dirName.startswith("Z")):
            ##dirName = 'B:/Hub EDI Guidelines' + dirName
            dirName = "C:/specService/Hub EDI Guidelines/" + dirName

            if not os.path.exists(os.path.join(dirName, './Production Specs')):
                noCurrent = True
                subDir = False

                for newDir in os.walk(dirName).next()[1]:

                    if "Current".lower() in newDir.lower():
                        try:
                            os.rename(os.path.join(dirName, newDir), os.path.join(dirName, './Production Specs'))
                            noCurrent = False
                            newDir = dirName + "/Production Specs"
                            renamedFolders.write(newDir + '\n')

                            for sub in os.walk(newDir).next()[1]:
                                sub = newDir + "/" + sub
                                if (os.path.isdir(sub)):
                                    subDir = True
                        except:
                            denied.write(dirName + '\n')
                            print("file open, cant rename " + dirName)

                if noCurrent:
                    os.makedirs(os.path.join(dirName, './Production Specs'))
                    noCurrentFolder.write(dirName + '\n')
                if subDir:
                    subFolders.write(dirName + '\n')
            else:
                noWork.write(dirName + '\n')
                for newDir in os.walk(dirName).next()[1]:
                    if "Current".lower() in newDir.lower():
                        double.write(dirName + '\n')
                        print("Shame on whoever did this" + dirName)

if __name__ == "__main__":
    renameSpecs()
