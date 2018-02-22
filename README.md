# py-pastpaper
A small tool for finding a specified substring in a directory of PDF files, using PyPDF2.  As of yet, this has only been tested on Windows, but it should work on other platforms.  This hasn't existed for very long, so it may be buggy.

## Usage
1. Specify a directory path that contains the PDFs you want to search through.
2. Specify a substring that you would like to search for.
3. If you want the search to be case-sensitive, tick the "Case sensitive" checkbox
4. Press "Search".

## Building (actually freezing)
I have used PyInstaller to generate a stand-alone executable.  Install [**Python 3.6**](https://www.python.org/) and [**PyPDF2**](http://mstamy2.github.io/PyPDF2/), and run **pyinstaller-windows.bat**.  As you may be able to tell, this will only work on Windows (probably).  That's not to say that it is impossible to freeze Python programs and target other platforms.

## Why the weird name?
I made it to match questions from mixed up exam papers to their mark schemes.
