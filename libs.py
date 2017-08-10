import sysconfig
import subprocess

def cflags():
    sysconfig.get_config_var('VCLibrarianTool')
    print('/LD ' + sysconfig.get_paths()['stdlib'] + '\\python' + sysconfig.get_config_vars()['py_version_nodot'] + '.lib')

cflags()
