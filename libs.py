import sysconfig

def cflags():
    sysconfig.get_config_var('CFLAGS')
    print('-l/' + sysconfig.get_paths()['stdlib'])

cflags()
