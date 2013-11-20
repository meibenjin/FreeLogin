#!/bin/bash

# user_name and passwd for slaves hosts
user_name="root"
user_pass="111111"

if [ $# != 1 ]; then
    echo "need ip list file"
    exit
fi
ip_list_file=$1

# first invoke free_python.py to setup passphraseless ssh to
# all hosts in ip list file 

`./free_login.py ${ip_list_file} ${user_name} ${user_pass}`
