import sysconfig
import subprocess

def cflags():
    sysconfig.get_config_var('cflags')
    print('/I ' + sysconfig.get_paths()['include'])

cflags()
