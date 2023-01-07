# MkDocs / Install MkDocs

MkDocs installation steps are described on the [MkDocs website](http://www.mkdocs.org/) and are summarized below
to verify that the steps work on different operating systems.

MkDocs requires Python.
Python may not otherwise be utilized in a software or documentation project and
in such cases Python will only be used behind the scenes.
On the other hand, Python may be utilized as the primary language for a software project, or may be used
as a supporting utility language for scripting.  Python is available on common operating systems.

It may be necessary or desirable to use a third-party MkDocs theme to enable an improved look and feel and functionality.
This decision may not be obvious until after content has been added to the documentation.
The following are links to themes:

*   [MkDocs Themes on GitHub](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
*   [Material Theme](http://squidfunk.github.io/mkdocs-material/) - this documentation uses Material theme
*   [MkDocs Bootswatch Project Themes on GitHub](http://mkdocs.github.io/mkdocs-bootswatch/)

To use a third-party theme, follow the link for the theme on the above page and follow installation instructions.
Note that in some cases the theme will already have been installed and `pip` will indicate that update can be used.
After installing the theme, change the `theme` configuration property in the `mkdocs.yml` file to indicate the new theme.
It may be necessary to and restart MkDocs (see [Edit Content section](edit.md)).

The following describes how to install MkDocs:

*   ![Cygwin](images/cygwin-32.png) [Install on Cygwin](#install-on-cygwin)
*   ![Linux](images/linux-32.png) [Install on Linux](#install-on-linux)
*   ![Windows](images/windows-32.png) [Install on Windows](#install-on-windows)
*   [Update MkDocs](#update-mkdocs)

-------

## ![Cygwin](images/cygwin-32.png) Install on Cygwin ##

The following instructions describe how to install MkDocs on Cygwin for Python 3 (`python3`).

### Install Python ###

Check to see if Python is installed on the system.  The `python3` program is used for Python3.
Note that the `python` program corresponds to Python 2 and care needs to be taken to use `python3`.

```sh
$ which python3
/usr/bin/python3

$ python3 --version
Python 3.6.4
```

If `python3` is not installed, install using the Cygwin installation tool.

### Install pip ###

MkDocs is installed using the `pip3` tool.
This is a script in addition to the `pip` module installed as a `python3` package.
Check whether `pip3` is installed:

```sh
$ pip3 --version
pip 9.0.1 from /usr/lib/python3.6/site-packages (python 3.6)
```

or equivalently:

```sh
$ python3 -m pip --version
pip 9.0.1 from /usr/lib/python3.6/site-packages (python 3.6)

```

The Windows output may be shown when run on Cygwin in this example because Cygwin will search for
software installed on Windows if not found on Cygwin.
This may be OK if MkDocs from Windows is used instead of Cygwin.
However, if it is desired to use Python and `pip` on Cygwin, confirm the installation on Cygwin.

If `pip` is not installed for `python3`, install it.
Even though pip should already be included with `python3` on Cygwin, it may not actually have been installed
(see [Stack Overflow article "Installing new versions of Pytnon on Cygwin does not install Pip?"](http://stackoverflow.com/questions/30863501/installing-new-versions-of-python-on-cygwin-does-not-install-pip)).
Following the instructions from the above link to install pip on Cygwin:

```sh
$ python3 -m ensurepip
```

### Install MkDocs ###

MkDocs is installed as a Python module.  First check whether MkDocs is installed:

```sh
$ mkdocs --version
mkdocs, version 1.0.4 from /usr/lib/python3.6/site-packages/mkdocs (Python 3.6)
```

If MkDocs is not installed, install and if necessary update `pip`:

```sh
$ pip3 install mkdocs
```

### Install MkDocs Theme ###

It is often useful to install a MkDocs theme.
For example, this documentation uses the Material theme.
To install, use a command similar to the following:

```sh
$ pip3 install mkdocs-material
```

## ![Linux](images/linux-32.png) Install on Linux ##

The following instructions describe how to install MkDocs on Linux.
The following examples used Debian Jessie, although other Linux distributions would be similar.
There may be variations in install locations and handling of Python program name for Python versions 2 and 3.
Therefore, it is important to understand what is installed and which program name should be used.
It is assumed that software is being installed on a virtual machine or other environment.
MkDocs is more appropriate for a developer computer than a server.
MkDocs has been verified to work with Python 2 (`python`) and Python 3 (`python3`).
The following focuses on newer `python3`.

### Install Python

Check to see if Python is installed on the system (the `python3` program corresponds to Python 3
and `python` corresponds to Python 2):

```sh
$ which python3
/usr/bin/python3

$ python3 --version
Python 3.4.2
```

If necessary, install Python:

```sh
$ sudo apt-get install python3
```

### Install pip ###

MkDocs requires that the `pip3` Python module is installed for `python3`.  Check whether `pip3` is installed:

```sh
$ which pip3
/usr/bin/pip3

$ pip3 --version
pip 1.5.6 from /usr/lib/python3/dist-packages (python 3.4)
```

If `pip3` is not installed, install it:

```sh
$ sudo apt-get install python3-pip
```

### Install MkDocs ###

MkDocs is installed as a Python module.  First check whether MkDocs is installed:

```sh
$ mkdocs --version
```

If MkDocs is not installed, install:

```sh
$ sudo pip3 install mkdocs

$ mkdocs --version
mkdocs, version 0.17.3
```

### Install MkDocs Theme ###

It is often useful to install a MkDocs theme.
For example, this documentation uses the Material theme.
To install, use a command similar to the following:

```sh
$ sudo pip3 install mkdocs-material
```

## ![Windows](images/windows-32.png) Install on Windows ##

The following instructions describe how to install MkDocs on Windows 7 & 10.
The following focuses on Python 3.

Note that the Python installation for Windows has changed over time.
Newer installations of Python recommend installing the software in a user's file locations,
which corresponds to `C:\Users\usr\AppData` rather than older `C:\Python27`, etc., in order
to minimize need for administrator privileges and avoid installing Python packages in a system folder.

Python software for new installations is also accessed using the `py` program.
The `py.exe` program is installed in `C:\windows` and therefore is always in the `PATH` environment variable.
The `py` program finds Python 2 and 3 versions on the system and by default runs the newest installed version.
This ensures that Python can be run without adding a specific Python installation folder to the `PATH`.
Of course, installing `py` requires administrative privileges even if the Python
software itself is installed in user files.
The benefit of installing Python in user files is that additional packages can be
installed without administrative privileges.

The following illustrates how Python is found on the command line:

```sh
>where python
INFO: Could not find files for the given pattern(s).

>where python3
INFO: Could not find files for the given pattern(s).

>where py
C:\Windows\py.exe
```

### Install Python ###

Check to see if Python is installed on the system.

#### Checking for Python using `py` ####

If `py` is used to run Python, available Python can be listed as following
(the asterisk indicates the version that will be used by default):

```sh
> py --list
Installed Pythons found by py Launcher for Windows
 -3.7-64 *
 -3.5-64
 -2.7-64

>py --version
Python 3.7.2
```

#### Checking for Python in `PATH` ####

If Python was added to the `PATH` then the following can be used to check whether it is installed:

```
> where python
C:\Users\xxx\AppData\Local\Programs\Python\Python35-32\python.exe

$ python --version
Python 3.5.1
```

Python may not have been added to the `PATH` environment variable.
If nothing is shown above, also check for Python installation in `C:\Users\xxx\AppData\Local\Program\Python\Python37`
(which is used for Python 3.7), although other locations may have been used,
such as `C:\Users\xxx\AppData\Roaming\Python\Python35`.

If necessary, install Python for Windows from the [Python download site](https://www.python.org/downloads/windows/).

### Install pip

MkDocs requires the `pip` Python module installation tool to be installed.  Check whether `pip` is installed:

```
> pip --version
pip 7.1.2 from c:\users\sam\appdata\local\programs\python\python35-32\lib\site-packages (python 3.5)
```

Because of the complexities of installing multiple Python versions,
it may be more clear to run `pip` by specifying as a module:

```
> py -m pip --version 

pip 18.1 from C:\Users\xxx\AppData\Local\Programs\Python\Python37\lib\site-packages\pip (python 3.7)
```

If `pip` is not installed, install it:

```
py -m ensurepip
```

### Install MkDocs ###

MkDocs is installed as a Python module.  First check whether MkDocs is installed:
```
> py -m mkdocs --version
__main__.py, version 1.0.4 from C:\Users\sam\AppData\Local\Programs\Python\Python37\lib\site-packages\mkdocs (Python 3.7)

```

If MkDocs is not installed, install.

```
> py -m pip install mkdocs
```

### Install MkDocs Theme ###

It is often useful to install a MkDocs theme.
For example, this documentation uses the Material theme.
To install, use a command similar to the following:

```sh
> py -m pip install mkdocs-material
```

## Update MkDocs ##

[MkDocs release notes](http://www.mkdocs.org/about/release-notes/) can be consulted to determine whether to update MkDocs.

New versions of MkDocs software can be installed by running the following, or a variation, as per operating system:

```sh
$ pip install --upgrade mkdocs
```

## Next Steps ##

After installing the software, the next step is to create a new MkDocs project to organize documentation files.
