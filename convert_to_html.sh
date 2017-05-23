# Convert notebook files *.ipynb to html
# Put the new files in html_versions directory

mkdir -p html_versions

for f in Index Hazard_Curves Hazard_Maps Make_Hazard_Curves_and_Maps
    do
      jupyter nbconvert --to html --execute $f.ipynb
      # change .ipynb to .html so links work to move between notebooks:
      sed s/ipynb/html/g $f.html > html_versions/$f.html
      rm -f $f.html
      echo Created html_versions/$f.html

    done

