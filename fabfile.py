from __future__ import with_statement
from fabric.api import *


def ec2():
    env.hosts = ['184.169.150.212']
    env.user = 'ec2-user'
    env.key_filename = 'C:\Users\kenliu\Downloads\sunnyliu.pem'

def deploy():
    run('cd ~; hostname; touch abc')
    

