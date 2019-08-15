import os

path = 'H:\Fronts\jan2019\correction(aug19)'

#os.chdir(path)

for filename in os.listdir(path):
    if filename.endswith('2.csv'):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:-1]
            print(lines)
        continue
   # else
    #    continue
#pam = os.getcwd()

