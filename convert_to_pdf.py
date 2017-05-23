
import re
import subprocess
import os, sys


notebooks = ['Index',
             'Hazard_Curves',
             'Make_Hazard_Curves_and_Maps']
#notebooks = ['Hazard_Maps']

title_text = str(r"""

 \newcommand{\altaffilmark}[1]{}

 \begin{centering}
{\LARGE Supporting Information for "Probabilistic Tsunami Hazard Analysis
(PTHA): multiple sources and global applications}


\vskip 10pt
{Andrey Babeyko\altaffilmark{1}, Maria Ana Baptista\altaffilmark{2}, J\"{o}rn
Behrens\altaffilmark{3}, Antonio Costa\altaffilmark{4}, Gareth
Davies\altaffilmark{5}, Eric L. Geist\altaffilmark{6}, Sylfest
Glimsdal\altaffilmark{7}, Frank I. Gonz\'{a}lez\altaffilmark{8}, Jonathan
Griffin\altaffilmark{5}, Carl B. Harbitz\altaffilmark{9}, Randall J.
LeVeque\altaffilmark{8}, Stefano Lorito\altaffilmark{10}, Finn
L{\o}vholt\altaffilmark{7}, Rachid Omira\altaffilmark{2}, Christof
Mueller\altaffilmark{11}, Rapha\"{e}l Paris\altaffilmark{12}, Tom
Parsons\altaffilmark{6}, Jascha Polet\altaffilmark{13}, William
Power\altaffilmark{11}, Jacopo Selva\altaffilmark{4}, Mathilde B.
S{\o}rensen\altaffilmark{14}, Hong Kie Thio\altaffilmark{15}, Anita
Grezio\altaffilmark{4}}

\vskip 10pt
{\Large \color{blue} Jupyter notebook output from {\tt Index.ipynb}}

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
    

