import os, shutil, json, webbrowser
from pathlib import Path
from . import utils

d_params = utils.get_params()

SRC_DIR = Path(__file__).resolve().parent / 'files' / d_params['type']
DST_DIR = Path(os.getcwd()).resolve()

shutil.copy(src= SRC_DIR / '.babelrc' , dst= DST_DIR / '.babelrc' )
shutil.copy(src= SRC_DIR / 'webpack.config.js' , dst= DST_DIR / 'webpack.config.js' )

shutil.copytree(src= SRC_DIR / 'src' , dst= DST_DIR / 'src' )

pkg_mgr = d_params['pkg_mgr']

if pkg_mgr == 'npm':
    os.system('npm init -y')
else:
    os.system('pnpm init')

with open('package.json','r+') as file:
    data = json.load(file)
    data['scripts'] = {
        'start' : 'webpack-dev-server --mode=development',
        'build' : 'webpack --mode=production'
        }
    file.seek(0)
    json.dump(data, file, indent=4)

# install sass for sass-loader

str_react_libs = 'react react-dom'
str_babel_libs = '@babel/core @babel/preset-env @babel/preset-react'
str_webpack_libs = 'webpack webpack-cli webpack-dev-server html-webpack-plugin'
str_loaders_libs = 'babel-loader css-loader style-loader file-loader'

if d_params['type'] == 'website':
    str_react_libs += ' react-router-dom'
    str_loaders_libs +=  ' sass sass-loader'

if d_params['scope'] == 'local':
    os.system(f'{pkg_mgr} i {str_react_libs} --S')
    os.system(f'{pkg_mgr} i {str_babel_libs} {str_webpack_libs} {str_loaders_libs} --D')
else:
    if pkg_mgr == 'npm':
        os.system(f'npm link {str_react_libs} {str_babel_libs} {str_webpack_libs} {str_loaders_libs}')
    else:
        os.system(f'pnpm link -g {str_react_libs} {str_babel_libs} {str_webpack_libs} {str_loaders_libs}')

url = 'http://localhost:8080'

if d_params['type'] == 'website' :
    url += '/home'

webbrowser.open(url)

os.system(f'{pkg_mgr} run start')