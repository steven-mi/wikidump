import shutil
import glob
import os
from tqdm import tqdm

os.makedirs("cleaned", exist_ok=True)

files = glob.glob("de_corpus/*")
for file in tqdm(files):
    with open(file) as f:
        length = len(f.read())
        if length >= 1500:
            shutil.copy2(file, "cleaned")
