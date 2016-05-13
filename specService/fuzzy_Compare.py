from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import os
import csv
import collections
save_file = open('results.csv', 'w')
writer = csv.writer(save_file, lineterminator = '\n')
header_row = ['DC4 Company Name,Hub EDI Guidelines Folder,Percent Match']
writer.writerow(header_row)
company = {}
folders_found = []
if __name__ == "__main__":
    with open('dc4.txt') as dc4:
        data = {}
        for line in dc4:
            line = line.strip()
            #print line
            for dir_name in os.walk("Hub EDI Guidelines").next()[1]:
                score = fuzz.ratio(dir_name, line)
                if score >= 95:
                    if line in company:
                        company[line].append(dir_name + ',' + str(score))
                    else:
                        # create a new array in this slot
                        company[line] = [dir_name + ',' + str(score)]
                    folders_found.append(dir_name)
                    #print dir_name
                    #print('%d%% partial match: "%s" with "%s" ' % (score, dir_name, line))
                    Digi_Results = [line, dir_name, score]
                    writer.writerow(Digi_Results)

for key in company:
    keyValue = key + " - "
    for value in company[key]:
        print keyValue + value

#print [x for x in folders_found if folders_found.count(x) > 1]
save_file.close()
