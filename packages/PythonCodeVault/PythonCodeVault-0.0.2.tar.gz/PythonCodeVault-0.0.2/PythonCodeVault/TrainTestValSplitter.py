import os
from pathlib import Path
from tqdm import tqdm
from random import shuffle
import shutil

# TODO:
# - absolute splits


def ClassificationSplitter(base_dir = './data', folders = ['Pass', 'Fail'], splits_percent = [70,20,10], extension = 'png'):
    
    """
    Splits two directories (e.g. Fail & Pass) into Train and Test.

    Parameters
    ----------
    base_dir: str
        Base directory containing the Label directories

    folders: list of str
        containing Label folder names

    splits_percent: list
        containing splits in percent -> [train, test, val]
        0 means split will not be created
        -1 means split contains remaining percent

        
    Structure of given Base Folder should be like:

        Base
        │
        └─── Label0
        │    │   file01.txt
        │    │   ...
        │   
        └─── Label1
        │    │   file11.txt
        │    │   ...
        │   
        └─── Label2
            │   file21.txt
            │   ...
    """

    if sum(splits_percent) != 100 and -1 not in splits_percent: raise Exception('Sum of percentages has to be 100')
    if splits_percent.count(-1) > 1: raise Exception('Only one -1 alowed in splits_percent')

    # splits_percent exists and contains -1:
    if -1 in splits_percent:
        idx = splits_percent.index(-1)
        splits_percent[idx] = 100 - (sum(splits_percent) + 1)

    # src folder
    base_dir = os.path.abspath(base_dir)

    val = True
    if splits_percent[2] == 0:
        val = False
    
    # dest folders
    split_dir = os.path.join(base_dir, 'split')
    if os.path.exists(split_dir):
        shutil.rmtree(split_dir)
    Path(split_dir).mkdir(exist_ok=True)
    Path(os.path.join(split_dir, 'Train')).mkdir(exist_ok=True)
    Path(os.path.join(split_dir, 'Test')).mkdir(exist_ok=True)
    if val:
        Path(os.path.join(split_dir, 'Val')).mkdir(exist_ok=True)

    train_dest_folders = [os.path.join(split_dir, 'Train', label) for label in folders]
    test_dest_folders = [os.path.join(split_dir, 'Test', label) for label in folders]
    if val:
        val_dest_folders = [os.path.join(split_dir, 'Val', label) for label in folders]

    for new_folder in train_dest_folders: Path(new_folder).mkdir()
    for new_folder in test_dest_folders: Path(new_folder).mkdir()
    if val:
        for new_folder in val_dest_folders: Path(new_folder).mkdir()


    for folder in folders:
        src_folder = os.path.join(base_dir, folder)

        shuffled_filenames = [file for file in os.listdir(src_folder) if file.endswith(extension)]
        shuffle(shuffled_filenames)
        shuffle(shuffled_filenames)

        if splits_percent:
            train_size = int(len(shuffled_filenames) * splits_percent[0] / 100) + 1
            test_size = int(len(shuffled_filenames) * splits_percent[1] / 100)
            if val:
                val_size = int(len(shuffled_filenames) * splits_percent[2] / 100)

            train_filenames = shuffled_filenames[:train_size]
            test_filenames = shuffled_filenames[train_size:train_size+test_size]
            if val:
                val_filenames = shuffled_filenames[train_size+test_size:]

            for filename in train_filenames:
                src_file_path = os.path.join(base_dir, folder, filename)
                dest_file_path = os.path.join(split_dir, 'Train', folder, filename)
                shutil.copy(src_file_path, dest_file_path)
            
            for filename in test_filenames:
                src_file_path = os.path.join(base_dir, folder, filename)
                dest_file_path = os.path.join(split_dir, 'Test', folder, filename)
                shutil.copy(src_file_path, dest_file_path)

            if val:
                for filename in val_filenames:
                    src_file_path = os.path.join(base_dir, folder, filename)
                    dest_file_path = os.path.join(split_dir, 'Val', folder, filename)
                    shutil.copy(src_file_path, dest_file_path)