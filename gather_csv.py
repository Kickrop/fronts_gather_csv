import os

path = 'H:\Fronts\jan2019\correction(aug19)'

os.chdir(path)

with open('1.csv', 'r') as f:
    lines = f.readlines()[2:-2]
    with open('text.csv', 'a') as nf:
        for i in lines:
            nf.write(i)
    print(lines)
#        continue
   # else
    #    continue
#pam = os.getcwd()

