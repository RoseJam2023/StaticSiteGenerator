#!/bin/bash

if [ -z "$1" ]
then
    python3 -m unittest discover -s src
else
    PYTHONPATH=src python3 -m unittest $1
fi