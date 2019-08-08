# -*- coding: utf-8 -*-
import os
import time
import sys
import subprocess


version_file = 'version.txt'


def prepare_version(version_number, commit):
    date_ = time.strftime('%Y%m%d')
    version = "ad-bypass.web.{0}.{1}.{2}".format(version_number, date_, commit)
    os.system('echo {} > {}'.format(version, version_file))
    os.system('git add {}'.format(version_file))
    tar_commit = subprocess.check_output('git stash create {}'.format(version_file))[0:8]
    return version, tar_commit


def publish():
    publish_version = raw_input('Enter the publish version:')
    if not publish_version:
        return
    commit = subprocess.check_output('git rev-parse --short HEAD').replace('\n', '')
    if not commit:
        return
    version, tar_commit = prepare_version(publish_version, commit)
    if not version:
        return
    os.system('git archive {0} --output={1}.tar.gz'.format(tar_commit, version))
    os.system('git rm -f {}'.format(version_file))


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        print "\n *** Wrong parameters! ***"
    else:
        action = argv[1]
        if action.lower() == 'publish':
            publish()
        else:
            print "\n *** Wrong parameters! ***"
