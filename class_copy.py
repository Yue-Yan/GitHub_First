# Author: Feiyue
# Date: 2022-08-19
# Diff: No different about code, just add this line.

import os
import json
import pandas as pd

class Test(object):
    def __init__(self, folder):
        self.folder = folder
    
    # get folder info
    def get_folder_info(self):
        directory = [item for item in os.listdir(self.folder) if not item.startswith(".")] 
        directory_name = [item.split("_")[2] for item in directory]
        print(f"There are {len(directory_name)}: directory_name")

    # get each language info
    def get_statistic_info(self):
        directory = [item for item in os.listdir(self.folder) if not item.startswith(".")]
        directory_csv = [os.path.join(self.folder, item) for item in directory]
        which_language = input("Choice one language: ")
        
        with open(which_language, 'r') as f:
            text = f.readlines()
	    filtered_text = [line.strip('\n') for line in text]
        
        data = [json.loads(line) for line in filtered_text]
        df = pd.DataFrame(data)

        print(f'Some basic info of this language: ', df.info())