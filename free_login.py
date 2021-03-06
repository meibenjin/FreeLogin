#!/usr/bin/python

import os
import pexpect
import sys

# generate public key
child = pexpect.spawn('ssh-key-gen -t rsa')
message = ''
try:
    child.expect('save the key')
    child.sendline('')
    child.expect('[Ee]nter passphrase')
    child.sendline('')
    child.expect('[Ee]nter samepassphrase again')
    child.sendline('')
except pexpect.EOF:
    message = child.read()
    child.close()
else:
    message = child.read()
    child.expect(pexpect.EOF)
    child.close()

ip_list = sys.argv[1]
user_name = sys.argv[2]
pwd = sys.argv[3]
file = open(ip_list,"r")
lines = file.readlines()
for line in lines:
    line = line.strip('\n')
    print "set free login on host:%s" % line
    child = pexpect.spawn('ssh-copy-id -i ${HOME}/.ssh/id_rsa.pub ' + user_name + '@' + line)
    message = ''
    try:
        i = child.expect(['[Pp]assword:','continue connecting'])
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
