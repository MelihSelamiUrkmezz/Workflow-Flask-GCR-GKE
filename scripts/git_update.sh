#!/bin/bash

image="gcr.io/kouyazlab-370817/gcexample"

#get timestamp for the tag
timestamp=$(date +%Y%m%d%H%M%S)

tag=$timestamp
echo $tag
