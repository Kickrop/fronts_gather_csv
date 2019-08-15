import os
from tqdm import tqdm

path = 'H:\Fronts\jan2019\correction(aug19)'

os.chdir(path)

#pam = os.getcwd()

for filename in tqdm(os.listdir(path)):
    if filename.endswith('.csv'):
        with open(filename, 'r') as f:
            lines = f.readlines()[2:-2]
            with open('gathered.csv', 'a') as nf:
                for i in lines:
                    nf.write(i)
        #print(lines)

