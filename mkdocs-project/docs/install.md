# Learn MkDocs / Install MkDocs

MkDocs installation steps are described on the [MkDocs website](http://www.mkdocs.org/) and are summarized below
to verify that the steps work on different operating systems.

MkDocs requires Python.
Python may not otherwise be utilized in a software or documentation project and
in such cases Python will only be used behind the scenes.
On the other hand, Python may be utilized as the primary language for a software project, or may be used
as a supporting utility language for scripting.  Python is available on common operating systems.

* [Install on Cygwin](#install-on-cygwin)
* [Install on Linux](#install-on-linux)
* [Install on Windows](#install-on-windows)
* [Install a Third-Party MkDocs Theme](#install-a-third-party-mkdocs-theme)
* [Update MkDocs](#update-mkdocs)

-------

## Install on Cygwin ##

The following instructions describe how to install MkDocs on Cygwin for Python 2 (`python`).

### Install Python ###

Check to see if Python is installed on the system (`python3` would be used for Python3):

```bash
$ which python
/usr/bin/python

$ python --version
Python 2.7.10
```

If Python is not installed, install Python using the Cygwin installation tool.

### Install pip ###

MkDocs requires the `pip` Python module installation tool to be installed.  Check whether `pip` is installed:

```bash
$ pip --version
pip 6.1.1 from /usr/lib/python2.7/site-packages (python 2.7)
```

The Windows output may be shown when run on Cygwin in this example because Cygwin will search for software on Windows if not found on Cygwin.
This is generally OK.

If `pip` is not installed, install it.
Even though pip should already be included with Python on Cygwin, it may not actually have been installed
(see [Stack Overflow article "Installing new versions of Pytnon on Cygwin does not install Pip?"](http://stackoverflow.com/questions/30863501/installing-new-versions-of-python-on-cygwin-does-not-install-pip)).
Following the instructions from the above link to install pip on Cygwin:

```bash
$ python -m ensurepip
Ignoring indexes: https://pypi.python.org/simple
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-6.1.1 setuptools-15.2
```

### Install MkDocs ###

MkDocs is installed as a Python module.  First check whether MkDocs is installed:

```bash
$ mkdocs --version
```

If MkDocs is not installed, install and if necessary update `pip`:

```bash
# There is some evidence that it needs to be installed from the developer's home folder
$ cd
$ pip install mkdocs

You are using pip version 7.1.2, however version 8.1.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

$ python –m pip install --upgrade pip

$ mkdocs --version
mkdocs, version 0.15.3

```

## Install on Linux ##

The following instructions describe how to install MkDocs on Linux, in this case Debian Wheezy,
although other Linux distributions would be similar.
MkDocs has been verified to work with Python2 but Python3 had an issue.
Therefore the following focuses on Python2.

***Follow IT system conventions.
It may be appropriate to install as root for all users (by using `sudo` or as a specific user.***

### Install Python

Check to see if Python is installed on the system (`python3` would be used for Python3):

```bash
$ which python
/usr/bin/python

$ python --version
Python 2.7.3
```

If necessary, install Python:


```bash
$ sudo apt-get install python
```

### Install pip ###

MkDocs requires that `pip` Python module installation tool to be installed.  Check whether `pip` is installed:

```bash
$ pip --version
pip 1.1 from /usr/lib/python2.7/dist-packages (python 2.7)
```

If `pip` is not installed, install it:

```bash
$ sudo apt-get install python-pip
```

### Install MkDocs ###

MkDocs is installed as a Python module.  First check whether MkDocs is installed:

```bash
$ mkdocs --version
```

If MkDocs is not installed, install:

```bash
# There is some evidence that it needs to be installed from the developer's home folder
$ cd
$ pip install mkdocs

$ mkdocs --version
mkdocs, version 0.15.3
```

## Install on Windows ##

The following instructions describe how to install MkDocs on Windows 7 & 10.
The following focuses on Python 3.

### Install Python ###

Check to see if Python is installed on the system.

```
> where python
C:\Users\sam\AppData\Local\Programs\Python\Python35-32\python.exe

$ python --version
Python 3.5.1
```

Python may not have been added to the `PATH` environment variable but generally is when installed.
If nothing is shown above, also check for Python installation in `C:\Python27`, `C:\Python35` and similar folders.

If necessary, install Python for Windows from the Python download site.

### Install pip

MkDocs requires the `pip` Python module installation tool to be installed.  Check whether `pip` is installed:

```
$ pip --version
pip 7.1.2 from c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages (python 3.5)
```

If `pip` is not installed, install it:

```
python -m pip install -U pip
```

### Install MkDocs ###

MkDocs is installed as a Python module.  First check whether MkDocs is installed:

```
$ mkdocs --version
```

If MkDocs is not installed, install.
There is some evidence that it needs to be installed from the developer's home folder.

```
C:
cd \Users\userName
pip install mkdocs

mkdocs --version
mkdocs, version 0.15.3
```

## Install a Third-Party MkDocs Theme ##

It may be necessary or desirable to use a third-party MkDocs theme to enable an improved look and feel and functionality.
This decision may not be obvious until after content has been added to the documentation.
The following are links to themes:

* [MkDocs Themes on GitHub](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
* [Material Theme](http://squidfunk.github.io/mkdocs-material/)
* [MkDocs Bootswatch Project Themes on GitHub](http://mkdocs.github.io/mkdocs-bootswatch/)

To use a third-party theme, follow the link for the theme on the above page and follow installation instructions.
Note that in some cases the theme will already have been installed and `pip` will indicate that update can be used.

After installing the theme, change the `theme` configuration property in the `mkdocs.yml` file to indicate the new theme.
It may be necessary to and restart MkDocs (see [Edit Content section](edit)).

## Update MkDocs ##

[MkDocs release notes](http://www.mkdocs.org/about/release-notes/) can be consulted to determine whether to update MkDocs.

New versions of MkDocs software can be installed by running the following
(may need to additionally use `--user` if Python modules have been installed in user files):

```sh
$ pip install --upgrade mkdocs
```

## Next Steps ##

After installing the software, the next step is to create a new MkDocs project to organize documentation files.
