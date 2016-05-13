import os
import shutil

DC4List = ['Associated Grocers of Florida Inc','Access Display Group Inc','Anderson Merchandisers','Aramark Uniform Services','Access Business Group - Vendorship','Access Business Group Procurement','AM General LLC','Arctic Zero Inc','ATT New Horizons','Alcatel Lucent Technologies','Arch Coal Inc','Auto Anything','Archbrook Laguna LLC','Arrow Speed Warehouse','Atwoods Distributing','Avnet Inc','American LaFrance','American Signature, Inc','AmerisourceBergen','Archer Daniels Midland Company','Assa Abloy Graham','Associated Food Stores DSD Xdock','Associated Grocers of New England','Associated Grocers of the South DSD']
specList = ['Associated Grocers of Florida, Inc','Access Display Group, Inc','Anderson Merchandiser','Aramark Uniform Service','Access Businees Group - Vendorship','Access Business Group - Procurement','AM General, LLC','Arctic Zero, Inc','AT&T New Horizons','Alcatel-Lucent Technologies','Arch Coal, Inc','AutoAnything','ArchBrook Laguna LLC','Arrow-Speed Warehouse','Atwoods Distribution','Avnet, Inc','American Lafrance','American Signature Inc','AmeriSourceBergen','Archer Daniels Midland Companies','Assa Abloy - Graham','Associated Food Stores DSD-XDock','Associated Grocers of New England Inc','Associated Grocers of the South']

def rename():
    dir = "C:\SPSSpecService\EDI Guidelines"
    for dir_name in os.walk("EDI Guidelines").next()[1]:
        for i in range(len(specList)):
            if(dir_name == specList[i]):
                fullDir = os.path.join(dir,dir_name)
                os.rename(fullDir,os.path.join(dir,DC4List[i]))
                dir_name = "EDI Guidelines/" + DC4List[i]
                if(dir_name.startswith("A"):
                    if not os.path.exists(os.path.join(dir_name,'./Production Specs')):
                        if os.path.exists(os.path.join(dir_name,'./Current Specs')):
                            os.rename(os.path.join(dir_name,'./Current Specs'), os.path.join(dir_name,'./Production Specs'))

if __name__ == "__main__":
    rename()
