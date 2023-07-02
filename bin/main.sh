#!/usr/bin/env bash

DIR=$1
ls -la
ls -la $DIR
python /app/FrontMatterGenerator.py -d $DIR