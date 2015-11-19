"""
Conversion script for turning HR Open Standard wiki .md files into the HTML
equivalent file. It is meant to be run from the command line in OSX or Linux.

Usage (assumes this file exists at ~/mdToHTML/convert.py)
> cd path/to/md/files

To convert all files in the current directory:
> python ~/mdToHtml/convert.py

To convert specific files:
> python ~/mdToHtml/convert.py file1.md file2.md fileN.md

When converting files, the script will first delete any impacted html files
and remove the html_files folder. It will then copy the html_files directory 
from the mdToHtml directory (to keep it clean) and then recreate the html files.

Header, footer, CSS, and the HR Open Standards logo are all copied from 
mdToHtml/templates. 

(c) 2015 DirectEmployers Association and HR Open Standards

"""
import markdown, codecs, sys, os, shutil

# Path of this file. Ensures proper file placement when called from other dirs
current_path = os.path.dirname(os.path.realpath(__file__))

file_list = []
args_list = sys.argv # capture any arguments
del args_list[0] # we don't need the file name
if len(args_list)>0:
    # create list of files to convert and remove existing converted files
    for f in args_list:
        file_list.append(f)
        os.remove(f.split(".md")[0]+".html")
else:
    # if no files specified, convert all .md files in the calling folder
    files=os.listdir(".")
    for f in files:
        ext = f.split(".")[-1]
        if ext=="md":
            file_list.append(f)
        elif ext=="html": #remove ALL html files
            os.remove(f)

# read the header and footer html
header_file = codecs.open(current_path+"/templates/header.html", 
                          mode="r", encoding="utf-8")
header_source = header_file.read()
footer_file = codecs.open(current_path+"/templates/footer.html", 
                          mode="r", encoding="utf-8")
footer_source = footer_file.read()

# clear the existing html_files dir & recreate it. Ensures it's up to date.
try:
    shutil.rmtree("html_files")
except OSError:
    pass
os.makedirs("html_files")
for hf in os.listdir(current_path+"/templates/html_files"):
    shutil.copy(current_path+"/templates/html_files/"+hf,"html_files")

# convert the files
for f in file_list:
    output_name = f.split(".")[0]+".html"    
    print output_name
    md_file = codecs.open(f, mode="r", encoding="utf-8",errors="ignore")
    md_source = md_file.read()
    html_source = markdown.markdown(md_source)
    html_source = "%s%s%s" % (header_source,html_source,footer_source)
    html_file = codecs.open(output_name,"w",encoding="utf-8",
                            errors="xmlcharrefreplace")
    html_file.write(html_source)

print "Done. %s file(s) converted." % len(file_list) 
