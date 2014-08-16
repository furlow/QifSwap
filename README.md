QifSwap
=======

QifSwap is a really simple application to automate the mundane task of importing transactions into YNAB (or other financial software) from credit card accounts (Lloyds, Halifax) which have the polarity of transactions inverted. 

This app swaps the polarity of the transactions so that the credit card accounts can be used in YNAB.

To run this app on any platform
===============================
The only prerequisite required is pyside and to install simply use:

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

Build for Linux
===============
Build instructions for linux will follow, however since adobe air is not offical supported for linux and although Ynab works through wine. Therefore I will create build instructions later.

Binaries
========

Binaries will be distributed soon for Windows, Mac and Linux.
