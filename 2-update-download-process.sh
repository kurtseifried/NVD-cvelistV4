#!/bin/bash


mkdir data
cd data

#
# Get NVD files. This will break in 2025.
#
wget -i ../file-list-updates.txt

gzip -d *.gz

#
# Convert the files to cve JSON entries
#

for file in *.json; do
    # Call the Python script with appropriate arguments
    ../process-file.py --output_dir ../cves/ "$file"
done


#cd ..
#rm -rf data
