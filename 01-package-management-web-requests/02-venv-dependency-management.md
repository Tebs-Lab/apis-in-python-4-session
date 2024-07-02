# Installing and Manging Python Libraries

Python has several 3rd party libraries which expand Python's functionality, but are not built into the language itself. We need one such libraries for today's lesson. Specifically we'll be installing the `requests` library to help us make web requests.

## A Note on Virtual Environments

A "virtual environment" in Python is a separate place to install libraries on a per-virtual-environment basis. Using these is considered a best practice (for many good reasons). The short version is that different software projects may require **specific versions** of individual software libraries, and virtual environments allow us to do this on a single computer.

For more about why a virtual environment is a good idea, read this: [https://realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/)

There are many competing tools for creating and managing virtual environments. In this walkthrough we're using the only one that is built into Python, called `venv`. You will quite likely encounter alternatives such as `conda`/Anaconda Navigator, `pipenv`, `poetry`, or others. You may ultimately wish to use one or more such packages as you become more familiar with building software in Python. Most of what you learn about `venv` will carry over to using these packages.

### Create a Virtual Environment

In your terminal navigate to the folder containing this repo (the folder containing the `readme.md` file), then run

```
python -m venv venv
```

The first part `python -m` tells python to run a particular module. The next part `venv` is the module that we specified. The third part (also `venv`) is the name of a folder (which is the virtual environment) that is created when we execute the command. 

We could have run `python -m venv my_env` and then that folder would have been named `my_env`. We chose `venv` because it is a common convention. You can also specify that this folder live anywhere on your computer. We prefer putting the virtual environment in the project folder, but that's mostly a matter of personal preference.

### Activate the Virtual Environment

When a virtual environment is "active" any python commands you run will use your virtual environment's version of python, and its set of libraries. If the virtual environment is not active, your system version of python will be used.

On Linux or MacOS systems run this command to activate:

```
source venv/bin/activate
```

On Windows Systems run this command to activate:

```
venv\Scripts\activate.bat
```

Or, if you're using PowerShell rather than the cmd prompt

```
venv\Scripts\Activate.Ps1
```

> On all systems, you can deactivate simply by running the command `deactivate` in your shell. 

### Now, we can install the libraries!

First, confirm that your virtual environment's version of `pip` is the one being used.

Linux/MacOS:

```
which pip
```

Windows cmd:

```
where pip
```

Windows Powershell

```
Get-Command pip
```

This should point to a file inside the `venv` folder we just created. Once you've confirmed that, run the following (on all systems this command is the same):

```
pip install requests fastapi
```

Now you should be able to run the python programs in this repo.