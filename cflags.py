import sysconfig
import subprocess

def cflags():
    sysconfig.get_config_var('include_dirs')
    print(sysconfig.get_paths()['include'] + '\\python.h')

cflags()
