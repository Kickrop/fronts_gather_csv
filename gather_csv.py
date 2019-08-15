import os
from tqdm import tqdm

path = 'H:\Fronts\jan2019\correction(aug19)'

os.chdir(path)

for filename in tqdm(os.listdir(path)):
    if filename.endswith('9999.csv'):
        with open(filename, 'r') as f:
            lines = f.readlines()[2:-2]
            with open('gathered.csv', 'a') as nf:
                for i in lines:
                    id_front = os.path.basename(filename.split('.')[0])
                    #write id_front and papers of that front in one csv
                    nf.write(f'"{id_front}",' + i)

