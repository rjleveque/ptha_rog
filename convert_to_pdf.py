"""
Convert notebooks to pdf format with header text containing
title and authors of main publication.
"""

from __future__ import print_function
import re
import subprocess
import os, sys

os.system('mkdir -p pdf_versions')  # create directory 

notebooks = ['Index',
             'Hazard_Curves',
             'Hazard_Maps',
             'Make_Hazard_Curves_and_Maps']

title_text = str(r"""

 \newcommand{\altaffilmark}[1]{}

 \begin{centering}
{\Large Supporting Information for }
\vskip 5pt
{\LARGE Probabilistic Tsunami Hazard Analysis
(PTHA): multiple sources and global applications}



\vskip 15pt
{\Large \color{blue} 
PTHA Tutorial
\vskip 5pt
Jupyter notebook output from {\tt Index.ipynb}
\vskip 5pt
Original notebooks and data can be found at\\
\url{https://doi.org/10.5281/zenodo.816290}.  }

\end{centering}

\vskip 10pt
""")


for i, notebook in enumerate(notebooks):
    filename = notebook + '.ipynb'
    print("Processing %s" % filename)
    with open(filename, "r") as source:
        lines = source.readlines()
    latex_filename = notebook+'.tex'
    pdf_filename = notebook+'.pdf'

    args = ["jupyter", "nbconvert", "--to", "latex", "--execute",
            "--ExecutePreprocessor.kernel_name=python2",
            "--ExecutePreprocessor.timeout=60", filename]
    subprocess.check_call(args)

    with open(latex_filename, "r") as source:
        lines = source.readlines()

    filename_str = re.sub('_','\\_', filename)
    this_title_text = re.sub('Index.ipynb', filename_str, title_text)
    
    with open(latex_filename, "w") as output:
        for line in lines:
            if 'maketitle' in line:
                line = this_title_text
            output.write(line)
            
    args = ["pdflatex", latex_filename]
    subprocess.check_call(args)
    subprocess.check_call(args) 
    

os.system('mv *.pdf pdf_versions')
print('Created pdf versions and moved them to subdirectory pdf_versions')
