import os
from tqdm import tqdm

path = 'H:\Fronts\jan2019\correction(aug19)'

os.chdir(path)

for filename in tqdm(os.listdir(path)):
    if filename.endswith('.csv'):
        with open(filename, 'r') as f:
            lines = f.readlines()[2:-2]
            with open('gathered.csv', 'a') as nf:
                for i in lines:
                    id_front = os.path.basename(filename.split('.')[0])
                    id_front_csv = f'"{id_front}",'
                    nf.write(id_front_csv + i)

