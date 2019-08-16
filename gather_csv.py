import os
from tqdm import tqdm

path = 'H:\Fronts\jan2019\correction(aug19)'

os.chdir(path)

output_filename = 'gathered'

#take second line from 1.csv file and write it as a header into created file
with open('1.csv', 'r') as f:    
    new_header = f.readlines()[1]
    with open(output_filename + '.csv', 'a') as nf:
        #add header for id_front values which will be created later
        nf.write(f'id_front,' + new_header)
    nf.close()
f.close()

for filename in tqdm(os.listdir(path)):
    if filename.endswith('.csv'):
        with open(filename, 'r') as f:
            lines = f.readlines()[2:-2]
            with open(output_filename + '.csv', 'a') as nf:
                for i in lines:
                    id_front = os.path.basename(filename.split('.')[0])
                    #write id_front and papers of that front in one csv
                    nf.write(f'"{id_front}",' + i)
            nf.close()
        f.close()
