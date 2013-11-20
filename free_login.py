#!/usr/bin/python

import os
import pexpect
import sys

file_path = sys.argv[1]
user_name = sys.argv[2]
pwd = sys.argv[3]
file = open(file_path,"r")
lines = file.readlines()
for line in lines:
    line = line.strip('\n')
    print "set free login on host:%s" % line
    child = pexpect.spawn('ssh-copy-id -i /root/.ssh/id_rsa.pub ' + user_name + '@' + line)
    message = ''
    try:
        i = child.expect(['[Pp]assword:','continue connecting (yes/no?)'])
        if i == 0:
            child.sendline(pwd)
        elif i == 1:
            child.sendline('yes')
            child.expect('[Pp]assword')
            child.sendline(pwd)
        else:
            pass
    except pexpect.EOF:
        message = child.read()
        child.close()
    else:
        message = child.read()
        child.expect(pexpect.EOF)
        child.close()
