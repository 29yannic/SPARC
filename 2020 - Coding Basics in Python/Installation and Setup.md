## Installation and Setup
The Python interpreter can be downloaded from the official python.org website https://www.python.org/downloads.


Usually the website should figure out which operating system you are using and display the correct version for that operating system of Python 3 to be downloaded by the click of a button.

Selecting the "Correct" Version
You will notice that there are many different versions of Python to chose from. In the "Maintenance status" column you can see different states of that version.

When it comes to software, having the newest version of something isn't always going to be the best option. That also goes for Python. Reasons why you should consider taking an older, often called "stable", release of Python or software in general are:

new features can contain bugs, these bugs are often fixed for older versions
you might not even need the newest features of a language
community support for older Python languages get's better the longer a version is around (until people stop using it due to new features becoming available on newer versions)
some modules or packages that you want to add to your project might not support the newest version of python
So given this information, and without the need for the latest features, the latest version of Python which is out of the "bugfix" state should be a good candidate.

For Windows Users
In order for you to be able to run Python from the command line and also inside the editor that we will be using, you need to make sure that you check the “Add python.exe to PATH” option when installing Python as seen in the Screenshot below.



## Installing Python Packages

With the installation of Python, a tool named “pip” should also be installed. pip is the package installer for Python that is used inside of the command line.

To find out which packages there are we can look at the “Python Packaging Index” or PyPI for short under https://pypi.org.

So since we want to use Phyton to remotely execute commands on a machine inside our network, we install the following package:
```
pip3 install networkdevice
```

To update the package, use
```
C:\Program Files\WinPython38_64bit\python-3.8.6.amd64\python.exe -m pip install --upgrade pip
```

After running this command, the networkdevice package should be successfully installed.
Please now hit 
```
pip3 list
```
This should give you an overview about the installed packages.