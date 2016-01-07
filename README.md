# xQuant
Code written for xQuant.com and financial studies during Dec. 2015 - Jan. 2016.

### Files

Details of each project should be seen in their respective README.

2.7 is for projects under python2.7 environment, which consists of:

* core.py: an attempt to extract specific financial related tables from pdf. This project is paused and passed over to Patrick Chen.

* django-calculator-microservice & django-ladon: both are forms of web-services that designed to handle requests, calculations and responses. They are cloned from https://github.com/jhonjairoroa87/django-calculator-microservice/ and https://github.com/TargetHolding/django-ladon respectively. I did some minor editing to learn how those tools work.

* xQuantWebCalculator: this is the main tool that I wrote for the web service tool my supervisor requested.



### Installations

#### VIRTUALENV
This repository consists of two python environments, one uses python2.7, the other uses python3.5. This was created by building virtural environments with [pyenv and virtualenv](http://amaral-lab.org/resources/guides/pyenv-tutorial), you can set up environments through the tutorial, and use
```
	pyenv local your_environment
```
to make sure everytime you enter the folder, such virtual environoment will be activated.

#### PIP installations.

In case you are missing other libarires, run pip (maybe pip install -r requirements.txt if it was kept clean enough) in the respective project folder to install necessary libraries. For details, read the README files in each directory.

<!-- ### Possible Errors
```
	* The following required packages can not be built:
    * freetype
```
If this error showed up, run 
```
	brew install freetype
``` -->

### After Thoughts

 **Recommend installing [Anaconda](https://www.continuum.io/downloads)**, as it contains a lot of resources to run the programs in this repository. It also serves as a virtual environment tool that can replace pyenv.

SEE THIS FOR MORE [DETAILS](http://stackoverflow.com/questions/34398676/does-conda-replace-the-need-for-virtualenv)

Also even the above practice of pip with python2.7 and python3.5 was later found to be sub-optimal for financial purposes, as pyenv does provide an anaconda version of python to be installed directly. What should be done is 
```
pyenv install anaconda3-2.4.0
pyenv virtualenv anaconda3-2.4.0 your_environment
pyenv local your_environment
```
However, the above method was untested, and only therotically working.

<!-- ##### IPython:
This was learned during the process, but did not end up using it. remember that IPython is an interactive shell for the Python programming language, so call it in bash instead of importing it in python (If using the shell version, the browser version requires pip install notebook and getting onto localhost).
 -->
