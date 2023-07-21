# React Project Generator

## Description
Python command line module to automatically create a minimal dependencies and basic react template. It implements `react-router-dom` already to manage different "pages".

The setup cames with the good practices like separated routes from the components, and the components by their own folders to define their styles in css and scss.

<br>

This app it's just tested on windows system.

- standard library modules used:
 - sys : build in module to manage specific parameters and function from the system.

 - pathlib : build-in module to manage file paths as objects.

- shutil : build-in module to manage  high level operations like copy files or directories.

- os : build-in module used as interface of the operative system.

- webbrowser : build-in module that provides high-level interface to manage a browser.

- json : build-in module to read and write json files.


## Setup

- Clone the repository anywhere in your local machine.

- Create a new system variable from envirorment variables named : PYTHONPATH

- Add the directory to PYTHONPATH to allow python have access to the module globally by using:
  
  ```cmd
  python -m module_name
  ```

- Create another folder where you want to create the React project.

- Open the terminal inside this new folder and type: 
```cmd
python -m react
```

- Wait until everything is set and a browser window will be open.

## Setup Troubles
- If you want to use the `--scope=global`, make sure to install the next requirements:

  ```cmd
  npm i -g react react-dom react-router-dom
  
  npm i -g @babel/core @babel/preset-env @babel/preset-react @babel/core @babel/preset-env @babel/preset-react
  
  npm i -g webpack webpack-cli webpack-dev-server html-webpack-plugin
  
  npm i -g babel-loader css-loader style-loader sass sass-loader file-loader
  ```
  if you want to use the `--pkg_mgr=pnpm` then change the requirement commands from npm to pnpm.
  
  PNPM will be much faster and less error verbose while setting up the project.

## Arguments:

- scope :
  - --scope=global ( default )
  - --scope=local
<br><br>
- pkg_mgr ( package manager ) :
  - --pkg_mgr=npm ( default )
  - --pkg_mgr=pnpm

- type :
  - --type=basic ( default )
  - --type=website ( adds navbar & router )

## Future Work
- Add common components that use Hooks as example.
- Implement generic useContext to the Navigation Bar.

## Screenshots
### Terminal
![cmd_hfAYrOH0lz](https://user-images.githubusercontent.com/36393143/205958747-4e4fdbae-4da3-4547-9b97-3e50ba9c34cc.png)

### Main Screen
![O2Li5X63D1](https://user-images.githubusercontent.com/36393143/205959165-3d7c9c80-d1cf-4ba9-867d-d31e5d099f50.png)