FreeLogin
=========

a tool for setup passphraseless ssh(自动化配置SSH无密钥登录)


How To Use ?

Install pexpect module
  tar -xzvf pexpect-2.3.tar.gz
  cd pexpect-2.3
  sudo python ./setup.py install

Download free_login.sh & free_login.py.
  chmod 744 free_login.sh
  chmod 744 free_login.py

Create a ip list file and put all the ip addresses which you want to free login into the file, one line per ip. like this

  192.168.0.100
  192.168.0.101
  192.168.0.102
  
