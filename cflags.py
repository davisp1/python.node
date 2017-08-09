import sysconfig

def cflags():
    sysconfig.get_config_var('CFLAGS')
    print('-I' + sysconfig.get_paths()['include'] + '\\python.h')

cflags()
