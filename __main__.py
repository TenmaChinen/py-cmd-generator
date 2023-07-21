from pathlib import Path
import shutil
import os

SRC_DIR = Path(__file__).resolve().parent / 'files'
DST_DIR = Path(os.getcwd()).resolve()

l_file_names = ['assets','components','app.py','controller.py','model.py','view.py']

for file_name in os.listdir(SRC_DIR):
    
    src_file_path = SRC_DIR / file_name
    dst_file_path = DST_DIR / file_name
    
    if os.path.isfile(path=src_file_path):
        shutil.copy(src=src_file_path, dst=dst_file_path)
    elif os.path.isdir(src_file_path):
        shutil.copytree(src=src_file_path, dst=dst_file_path)
