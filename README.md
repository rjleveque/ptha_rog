# ptha_rog
Draft notebooks for review paper on PTHA

Open the notebook [Contents.ipynb](Contents.ipynb) 
for the suggested order to view the other notebooks.

### View on Github

You can view static versions of the notebooks on the Github page by clicking
on a notebook in the list of files.  Note that the interactive widgets do not
work if you view them this way.

### Run the notebooks

To get the most out of these examples, you must run the notebooks so that the
interactive widgets work.  

You can either clone this repository and then use a Jupyter server
on your computer (see the [Jupyter documentation](http://jupyter.org/)),
or run them on the cloud (see below).

If you run them, make sure that you uncomment the line

    from ipywidgets import interact

and comment out the line

    from interact import interact

in order to get live widgets. The latter is used to produce figures that can be viewed from the Github webpage.

You can execute a single cell using `Shift-Enter`, or select `Run all` from the `Cell` menu to execute all cells and activate all widgets.

### Run on binder

You can use [binder](http://mybinder.org) to launch a notebook server in the
cloud from which you can run these notebooks from any web browser without
installing anything.  This may be slow to launch if binder is in heavy use:

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/rjleveque/ptha_rog)
