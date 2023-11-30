#!/bin/sh

./make-examples.sh && make clean && make html && make update && make clean

