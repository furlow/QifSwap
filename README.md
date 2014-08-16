QifSwap
=======

QifSwap is a really simple application to automate the mundane task of importing transactions into YNAB (or other financial software) from credit card accounts exported to qif  which have the polarity of transactions inverted. 

This app swaps the polarity of the transactions so that the credit card accounts can be used in YNAB.

To run this app on any platform
===============================
The prerequisites required is python and pyside. Search the internet on how to install python for you various platform. If installing on windows make sure to include the python path which is the last option in the list when installing.

Once python is installed open a terminal and install pyside

pip install pyside

Then execute QifSwap.py

Build for Windows
=================
To build for windows you will also need Py2exe:

pip install py2exe

To build run

python setup.py py2exe

The executable will be located in the dist folder

Build for Mac
=============
Instructions will follow shortly

Build for Linux
===============
Build instructions for linux will follow, since adobe air and ynab is not offically supported for linux, but is usuable through wine and special install scripts I will create build instructions later.

Binaries
========
Binaries will be distributed soon for Windows, Mac and Linux.
