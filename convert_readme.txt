
To convert notebooks to html files, do the following at bash prompt:

    source convert_to_html.sh

Resulting files are in html_versions subdirectory.

To convert notebooks to pdf files:

    python convert_to_pdf.py

Resulting files are in pdf_versions subdirectory.

Move to web server for viewing, do something like:
    scp html_versions/* rjl@homer.u.washington.edu:public_html/ptha_rog/
    scp pdf_versions/* rjl@homer.u.washington.edu:public_html/ptha_rog/
