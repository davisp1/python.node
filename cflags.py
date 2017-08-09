import sysconfig
import subprocess

#TODO: make it execute

def cflags():
    sysconfig.get_config_var('CFLAGS')
    print(sysconfig.get_paths()['include'])

cflags()
