import os
import re
from tqdm import tqdm

#path to downloaded fronts files in .csv
#path = 'H:\Fronts\jan2019\correction(aug19)'
path = 'H:/Fronts/jan2020/csv_files'
output_path = 'H:/Fronts/jan2020'

os.chdir(path)

output_filename = 'gathered'

#take second line from 1.csv file and write it as a header into created file
with open('1.csv', 'r') as f:    
    new_header = f.readlines()[1]   
    with open(output_filename + '.csv', 'a') as nf:
        #add header for front_name and id_front which values will be appended later
        nf.write(f'front_name,id_front,' + new_header)
    nf.close()
f.close()

#loop through all csv files in the folder
for filename in tqdm(os.listdir(path)):
    #os.chdir(path)
    if filename.endswith('.csv') and not filename.startswith(output_filename):
        with open(filename, 'r') as f:
            #take papers information only
            lines = f.readlines()
            first_line = lines[0]#f.readlines()#[0]
            papers = lines[2:-2]#f.readlines()[2:-2]    
            front_name = (re.search(r"(?<=')(.*)(?=')",first_line)).group()   
            #print(front_name,papers)
            #write id_front and papers of that front in one csv
            #os.chdir(output_path)
            with open(output_filename + '.csv', 'a') as nf:
                for i in papers:
                    id_front = os.path.basename(filename.split('.')[0])
                    nf.write(f'"{front_name}","{id_front}",' + i)
            nf.close()
        f.close()