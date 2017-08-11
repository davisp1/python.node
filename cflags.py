import sysconfig
import subprocess

def cflags():
    sysconfig.get_config_var('cflags')
    print(sysconfig.get_paths()['include'])

cflags()
