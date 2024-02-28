import os
import numpy as np
import random
from pathlib import Path
import matplotlib as mpl
mpl.rcParams['figure.max_open_warning'] = 0
import matplotlib.pyplot as plt


class Visualize3D():

        def __init__(self, dir_path:str):
                super(Visualize3D, self).__init__()
                if not os.path.exists(dir_path):
                        return None
                else:   
                        self.dir_path = dir_path 
        
                if os.path.isdir(self.dir_path):
                        print("We have got a directory path....")
                        print("Randomly selecting a sample from directory....")
                        random_file = self.__getrandomfile__(self)
                        if random_file is not None:
                                self.file_name = Path(random_file)
                        else:
                                self.file_name = None
                        print("Done.")
                elif os.path.isfile(self.dir_path):
                        print("File path is given.")
                        self.file_name = Path(self.dir_path)
    
        def __repr__(self):
                return f"aajna.vis.three.Visualize3D(data = {os.path.basename(self.file_name) if self.file_name is not None else self.file_name})"
                
            
        @staticmethod   
        def __getrandomfile__(self):
                all_files =  os.listdir(self.dir_path)
                file_list = [os.path.join(self.dir_path, f) for f in all_files]

                if len(file_list) == 0:
                        print(f"Directory {self.dir_path} is empty.")
                        return None
                else:
                        return random.choice(file_list)

        def inspect_npz(self):
                data = np.load(self.file_name)
                keys = data.files
                for i in keys:
                    if data[i].shape == (3,):
                        spacing_key = i
                length = data[keys[0]].shape[0]
                keys.remove(spacing_key)
                return (keys, spacing_key, length)
            

        def visual_2d_npz(self, figsize:tuple):
                data = np.load(self.file_name)
                plt.cla()
                plt.clf()
                plt.close('all')
                key = self.inspect_npz()[0]
                num_slices = self.inspect_npz()[-1]
                for i in range(num_slices):
                    plt.figure(figsize=figsize)
                    for j in range(len(key)):
                        
                        # Display the image
                        plt.subplot(1, len(key), j+1)
                        plt.imshow(data[key[j]][i], cmap='gray')
                        plt.title(f'{key[j]} - Slice {i + 1}')
                        plt.axis('off')