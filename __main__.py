import subprocess, shutil, json, sys, os
from pathlib import Path
from . import utils

SRC_DIR = Path(__file__).resolve().parent
DST_DIR = Path(os.getcwd()).resolve()

app_name = utils.get_app_name()

#########################################
#######   D J A N G O   C M D S   #######
#########################################

os.system('django-admin startproject app .')
os.system(f'python manage.py startapp {app_name}')

#########################################
###############   A P P   ###############
#########################################

utils.settings_modificator(SRC_DIR, DST_DIR , app_name)

src_file_path = SRC_DIR / 'files' / 'app' / 'urls.py'
dst_file_path = DST_DIR/ 'app' / 'urls.py'
utils.set_app_urls(src_file_path, dst_file_path, app_name)

#########################################
##############   F O O S   ##############
#########################################

for file_name in ['views.py', 'static', 'templates','urls.py','forms.py','models.py']:
   src_file_path = SRC_DIR / 'files' / 'foos' / file_name
   dst_file_path = DST_DIR / app_name / file_name

   if os.path.isfile(src_file_path):
      shutil.copy(src=src_file_path, dst=dst_file_path)
      utils.replace_foos(file_path=dst_file_path, app_name=app_name)
      # utils.replace_text(file_path=dst_file_path, src='foos', dst=app_name)

   elif os.path.isdir(src_file_path):
      shutil.copytree(src=src_file_path, dst=dst_file_path)

static_dir_path = DST_DIR / app_name / 'static' 
os.rename( static_dir_path / 'foos' , static_dir_path / app_name ) 

templates_dir_path = DST_DIR / app_name / 'templates' 
os.rename( templates_dir_path / 'foos' , templates_dir_path / app_name ) 

for template in ['create','list','update','delete']:
   file_path = templates_dir_path / app_name / f'{template}.html' 
   utils.replace_foos(file_path, app_name)

#########################################
############   G L O B A L   ############
#########################################

for directory in ['staticfiles', 'templates']:
   src_dir_path = SRC_DIR / 'files' / 'global' / directory
   dst_dir_path = DST_DIR / directory
   shutil.copytree(src=src_dir_path, dst=dst_dir_path)

#########################################
########   M I G R A T I O N S   ########
#########################################

os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

#########################################
########   S U P E R   U S E R   ########
#########################################

os.system('''python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('Superuser', '', 'superuser')"''')
