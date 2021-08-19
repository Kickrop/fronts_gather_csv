import os
import re
from tqdm import tqdm

#path to downloaded fronts files, .csv
path = r'D:/work/fronts/aug2021_стажеры'
output_path = 'D:/work/fronts/aug2021_output/'
output_filename = 'gathered'

def list_full_paths(path):
    return [os.path.join(path, file) for file in os.listdir(path)]

def get_header():
    with open(list_full_paths(path)[0], 'r') as f:
        #get the first line of the first file in folder  
        file_header = f.readlines()[1]

        #add new columns
        new_header = (f'front_name,id_front,' + file_header)
        f.close()
    return new_header   

def get_data_from_csvs(output_path,output_filename):
    list_of_papers = []
    for filename in tqdm(list_full_paths(path)):
        if filename.endswith('.csv') and not filename.startswith(output_filename):
            try:
                with open(filename, 'r') as f:
                    #take papers information only
                    lines = f.readlines()

                    #get the first line which contains name of the front
                    first_line = lines[0]
                    #extract name of the front from the first line
                    front_name = (re.search(r"(?<=')(.*)(?=')",first_line)).group()

                    #get the papers' data only
                    papers = lines[2:-2]    
                       
                    #for each paper in the front add front_name and id_front 
                    for i in papers:
                        #get id_front from the name of file
                        id_front = os.path.basename(filename.split('.')[0])
                        list_of_papers.append(f'"{front_name}","{id_front}",' + i)
                f.close()                 
            except:
                print('somethings not right')                 
    with open(output_path + output_filename + '.csv', 'a') as nf:
        nf.write(get_header())
        for paper in list_of_papers:
            nf.write(paper)

get_data_from_csvs(output_path,output_filename)
