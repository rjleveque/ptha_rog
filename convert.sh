# Convert notebook files *.ipynb to html and pdf
# Put the new files in ptha_rog_files directory

mkdir -p ptha_rog_files

for f in Index Hazard_Curves Hazard_Maps Make_Hazard_Curves_and_Maps
    do
      jupyter nbconvert --to html --execute $f.ipynb
      # change .ipynb to .html so links work to move between notebooks:
      sed s/ipynb/html/g $f.html > ptha_rog_files/$f.html
      rm -f $f.html
      echo Created ptha_rog_files/$f.html

      jupyter nbconvert --to pdf --execute $f.ipynb
      mv -f $f.pdf ptha_rog_files/
      echo Created ptha_rog_files/$f.pdf
    done

# Move to web server for viewing:
#scp ptha_rog_files/* rjl@homer.u.washington.edu:public_html/ptha_rog/
