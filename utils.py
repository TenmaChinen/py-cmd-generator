import sys

def get_app_name():

    l_args = sys.argv[1:]
    d_params = dict( app_name = 'foos' )

    for arg in l_args:
        if arg.__contains__('--') and arg.__contains__('='):
            arg = arg.strip('--')
            key, value = arg.split('=')
            if key in d_params:
                d_params[key] = value
                continue

        print(f'\n    Arg : {arg} is not valid\n\n    Params must be:')
        print(f'        --app_name=foo\n')
        sys.exit()
    else:
        return d_params['app_name']

def replace_text(file_path, src, dst):
  file = open(file_path, 'r+')
  text = file.read()
  text = text.replace(src, dst)
  file.seek(0)
  file.write(text)
  file.close()

def replace_foos(file_path, app_name):
  string = load(file_path)

  section_singular = app_name[0:-1]

  t_replaces = (
      ('footer', 'reserved'),
      ('Foo', section_singular.capitalize()),
      ('foo', section_singular),
      ('foos', app_name),
      ('reserved', 'footer')
      )

  for target, replace in t_replaces:
      string = string.replace(target, replace)

  save(file_path, string)


def settings_modificator(src_dir, dst_dir, app_name):

  settings_file_path = dst_dir / 'app' / 'settings.py'
  string = load(settings_file_path)
  
  #####################################
  ###########   H O S T S   ###########
  #####################################

  target = 'ALLOWED_HOSTS = []'
  replace = "ALLOWED_HOSTS = [ '127.0.0.1', 'teslachinen.pythonanywhere.com' ]"
  string = string.replace(target, replace)

  #####################################
  #######   T E M P L A T E S   #######
  #####################################

  target = "'DIRS': [],"
  replace = "'DIRS': [BASE_DIR / 'templates'],"
  string = string.replace(target, replace)

  #####################################
  ##   I N S T A L L E D   A P P S   ##
  #####################################

  target = "'django.contrib.staticfiles',"
  replace = f"{target}\n\t'{app_name}',"
  string = string.replace(target, replace)

  #####################################
  ##########   S T A T I C   ##########
  #####################################

  target = 'USE_TZ = True'
  start = string.find(target) + len(target)
  string = string[0:start] + '\n\n'

  extra = load(file_path= src_dir / 'files' / 'app' / 'settings_extra.py')
  string += extra

  save(file_path=settings_file_path, string=string)

def set_app_urls(src_file_path, dst_file_path, app_name):
  string = load(src_file_path)
  string = string.replace('foos', app_name)
  save(file_path=dst_file_path, string=string)


def load(file_path):
  file = open(file_path,'r')
  string = file.read()
  file.close()
  return string

def save(file_path, string):
  file = open(file_path,'w')
  file.write(string)
  file.close()
