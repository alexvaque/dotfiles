#/bin/bash

echo $1
python ec2s.py default us-east-1 --search=$1 

