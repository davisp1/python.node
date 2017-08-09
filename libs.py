import os
import sysconfig
import re

def cflags():
    sysconfig.get_config_var('CFLAGS')
    print('CL /MT ' + sysconfig.get_paths()['stdlib'] + '\\python27.lib')

cflags()
