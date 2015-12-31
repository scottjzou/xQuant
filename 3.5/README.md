# xQuant
Code written for xQuant.com and financial studies during Dec. 2015 - Jan. 2016

### Files


### Installations

#### Recommend installing [Anaconda](https://www.continuum.io/downloads), as it contains a lot of resources to run the programs in this repository. It also creates the virtuel


#### VIRTUALENV
ONLY DO THIS WHEN YOU DO NOT WANT TO USE ANACONDA

SEE THIS FOR MORE [DETAILS](http://stackoverflow.com/questions/34398676/does-conda-replace-the-need-for-virtualenv)

~~This environment uses python3.5, and was created in a virtural environment with [pyenv and virtualenv](http://amaral-lab.org/resources/guides/pyenv-tutorial), you can set up environments through the tutorial, and use
```
	pyenv local your_environment
```
to make sure everytime you enter the folder, such virtual environoment will be activated.
~~

The above practice was later found to be bad, as pyenv does provide an anaconda version of python to be installed directly. What should be done is 
```
pyenv install anaconda3-2.4.0
pyenv virtualenv anaconda3-2.4.0 your_environment
pyenv local your_environment
```
However, the above method was untested, and only therotically working. To 

##### PIP installations.

In case you are missing other libarires, run pip install -r requirements.txt to install necessary libraries.
```
	* The following required packages can not be built:
    * freetype
```
If this error showed up, run 
```
	brew install freetype
```
#### IPython:
This was learned during the process, remember that IPython is an interactive shell for the Python programming language, so call it in bash instead of importing it in python (If using the shell version, the browser version requires pip install notebook and getting onto localhost).

