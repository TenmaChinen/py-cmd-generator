from pathlib import Path
import shutil
import os

BASE_DIR = Path(__file__).resolve().parent
CUR_DIR = Path(os.getcwd()).resolve()

for file_name in ['index.html','style.css','script.js']:

	org_file_path = BASE_DIR / file_name
	copy_file_path = CUR_DIR / file_name
	shutil.copy(org_file_path, copy_file_path)