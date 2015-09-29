#!/usr/bin/env python

import sys, os

# get the script file name
try:
    script_path = sys.argv[1]
except IndexError:
    print 'require one argument as the script to run with python 2.7 + opencv 2.4.11'
    exit()


if os.path.isabs(script_path) is False:
    print 'pwd:', os.getcwd()
    script_path = os.getcwd() + '/' + script_path

script_name = script_path.split('/')[-1]

script_folder = None
# get the script folder path where the file stays
if script_name == script_path:
    script_folder = sbp.check_output('pwd')
else:
    script_folder = '/'.join(script_path.split('/')[0:-1])

arg_mount = '-v ' + script_folder + ':/exp'
arg_image = 'fatcloud/py27-cv24-gui-camera'
arg_cmd   = 'python ' + '/exp/' + script_name

args = [
    'docker run -it --rm',
    '-e DISPLAY',
    '-w /exp',
    '-v $HOME/.Xauthority:/home/developer/.Xauthority',
    '--net=host',
    '--privileged',
    arg_mount,
    arg_image,
    arg_cmd
]

cmd = ' '.join(args)

print '[py27-cv24] start running in bash:\n' + cmd
os.system(cmd)
