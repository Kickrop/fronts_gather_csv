import pandas as pd
import glob
import os


path = r'H:\Fronts\08_2019\new_papers\missing_wc'      # use your path
all_files = glob.glob(os.path.join(path, "*.txt"))     # os.path.join makes concatenation OS independent

df_from_each_file = (pd.read_csv(f,sep='\t',index_col=False) for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)