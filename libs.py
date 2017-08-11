import sysconfig
import subprocess

def libraries():
    sysconfig.get_config_var('libraries')
    print(sysconfig.get_paths()['stdlib'] + '\\python' + sysconfig.get_config_vars()['py_version_nodot'] + '.lib')

libraries()
