import sysconfig
import subprocess

#TODO: correct file

def cflags():
    sysconfig.get_config_var('VCCLCompilerTool')
    print(sysconfig.get_paths()['include'] + '\\python')

cflags()
