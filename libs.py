import sysconfig
import subprocess

def cflags():
    sysconfig.get_config_var('LIBS')
    print('-l ' + sysconfig.get_paths()['stdlib'] + '\\python27.lib')

cflags()
