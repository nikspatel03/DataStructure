"""
Crawling through directories and print out nested files and directories
with indentation
"""
import os

def crawl(filename, indent=""):
    if os.path.isfile(filename):
        print(filename)
    else:
         print(filename)
         directories = os.listdir(filename)
         print(directories)
         for file in directories:
             crawl(os.path.abspath(file), " ")


crawl("/users/npatel")
