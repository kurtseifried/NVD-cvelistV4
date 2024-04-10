#!/bin/bash

git pull

#./1-initial-download-process.sh

./2-update-download-process.sh

git add -A *

git commit -m "updates"

git push
