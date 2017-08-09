import sysconfig

def cflags():
    sysconfig.get_config_var('CFLAGS')
    print('CL /I ' + sysconfig.get_paths()['include'])

cflags()
