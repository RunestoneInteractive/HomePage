#!/bin/bash

pipenv run tinker --build
rsync -avz blog/html/ bnmnetp:/var/www/runestone/html/