#!/bin/bash

if [ -z "VIRTUAL_ENV" ]; then
   echo "please activate the rsdev environment"
   exit 1
fi

tinker --build
python3 make_sitemap.py
cp sitemap.xml blog/html/
rsync -avz -e 'ssh -i /Users/bmiller/.ssh/id_rsa' blog/html/ bnmnetp:/var/www/runestone/html/
