#!/bin/bash

if [ -z "VIRTUAL_ENV" ]; then
   echo "please activate the rsdev environment"
   exit 1
fi

tinker --build
rsync -avz -e 'ssh -i /Users/bradleymiller/.ssh/id_rsa' blog/html/ bnmnetp:/var/www/runestone/html/