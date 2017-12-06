
import subprocess
from subprocess import CalledProcessError
import os

class Source():

  def __init__(self, path):
    '''load shell variables as attributes from file at path'''
    cmd = '(. %s ; env | grep "=")' % (path)
    out = None
    try:
      out = subprocess.check_output(cmd, shell=True, universal_newlines=True)
    except CalledProcessError:
      print('cwd->' + os.getcwd())
      # lets see if we can convert to a non deployed path
      # eg ttse/env/env.sh -> ttse/src/main/env/env.sh
      cmd = cmd.replace('/', '/src/main/', 1) 
      out = subprocess.check_output(cmd, shell=True, universal_newlines=True)
      
    for line in out.splitlines():
      cols = line.split('=')
      if len(cols) == 2:
        setattr(self, cols[0], cols[1])
        #print('adding attribute self[%s]=%s', cols[0], cols[1])
