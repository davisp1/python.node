import sysconfig
import subprocess

def cflags():
    sysconfig.get_config_var('LIBS')
    print(sysconfig.get_paths()['stdlib'])

cflags()
