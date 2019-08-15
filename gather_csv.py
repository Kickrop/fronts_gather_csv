import os

path = 'H:\Fronts\jan2019\correction(aug19)'

os.chdir(path)

#pam = os.getcwd()

#for filename in os.listdir(path):
#    if filename.startswith('1.csv'):
#        with open('1.csv', 'r') as f:
#            lines = f.readlines()[2:-2]
#            with open('text.csv', 'a') as nf:
#                for i in lines:
#                    nf.write(i)
#        #print(lines)

for filename in os.listdir(path):
    if filename.startswith('1.csv'):
        alt_fn = filename.split('.')
        print(os.path.basename(alt_fn[0]))