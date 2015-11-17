# mdToHtml
Conversion script for turning HR Open Standard wiki .md files into the HTML
equivalent file. It is meant to be run from the command line in OSX or Linux.

## Usage 
Aassuming this file exists at ~/mdToHTML/convert.py:
```
> cd path/to/md/files
```

To convert all files in the current directory:
```
> python ~/mdToHtml/convert.py
```

To convert specific files:
```
> python ~/mdToHtml/convert.py file1.md file2.md fileN.md
```

When converting files, the script will first delete any impacted html files
and remove the html_files folder. It will then copy the html_files directory 
from the mdToHtml directory (to keep it clean) and then recreate the html files.

Header, footer, CSS, and the HR Open Standards logo are all copied from 
mdToHtml/templates. 

## Installing
Make sure you have pip installed:
OSX: 
```
> sudo easy_install pip
```

LINUX: 
```
> sudo apt-get install pip
```

It is recommended you create a virtual environment for this application. Instructions on doing so can be found here:
http://virtualenv.readthedocs.org/en/latest/installation.html

We also recommend VirtualenvWrapper, because it makes virtual envs so much easier:
http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation
 
(c) 2015 DirectEmployers Association
