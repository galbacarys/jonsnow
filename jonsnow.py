#!/usr/bin/env python3
# jonsnow.py
# 
# Night gathers, and now my watch begins. It shall not end until my death. I
# shall take no wife, hold no lands, father no children. I shall wear no crowns
# and win no glory. I shall live and die at my post. I am the sword in the
# darkness. I am the watcher on the walls. I am the fire that burns against the
# cold, the light that brings the dawn, the horn that wakes the sleepers, the
# shield that guards the realms of men. I pledge my life and honor to the
# Night's Watch, for this night and all the nights to come.
#
# But actually, this program watches a directory and executes an arbitrary
# command every time the contents of the directory changes.
#
# Examples:
#       jonsnow ./fight_white_walkers.sh
#       jonsnow echo "You know nothing..."
#       jonsnow if [ -z 'any shell scipting works' ]; then do_something.sh; fi

import os
import copy
import sys
import time
import subprocess

def usage():
    print('''
{}: Run commands on changes to any file in this directory

Usage: 
   jonsnow ./fight_white_walkers.sh
   jonsnow -r ../ echo "You know nothing..."

Arguments:
-r, --root PATH: specify the root directory you want {} to format.
                 Defaults to the current working directory.
--rtp PATH: Set the runtime path of the command you want to execute
            '''.format(sys.argv[0], sys.argv[0]))


def parse_arguments():
    ''' Parses arguments and returns values needed to run program.
    returns tuple of check_path, runtime_path, and the first index of argv that
    begins the actual command (in that order)
    '''
    check_path = None
    runtime_path = None
    latest_index = 1
    if '-r' in sys.argv:
        check_path = sys.argv[sys.argv.index('-r')]
        if latest_index < sys.argv.index('-r'):
            last_index = sys.argv.index('-r') + 1 # account for argument body
    elif '--root' in sys.argv:
        check_path = sys.argv[sys.argv.index('--root')]
        if latest_index < sys.argv.index('--root'):
            last_index = sys.argv.index('--root') + 1
    
    if '--rtp' in sys.argv:
        runtime_path = sys.argv[sys.argv.index('--rtp')]
        if latest_index < sys.argv.index('--rtp'):
            last_index = sys.argv.index('--rtp') + 1
    return (check_path, runtime_path, latest_index)

def check_tree(check_path, files):
    ''' Recursively checks for modification time on all files in tree
    '''
    for fi in os.scandir(check_path):
        if fi.is_dir():
            check_tree(fi.path, files)
        else:
            files[fi.path] = fi.stat().st_mtime

def resolve_changes(files, old_files):
    if len(files) != len(old_files):
        return True
    for filename in old_files:
        if not filename in files or files[filename] != old_files[filename]:
            return True
    return False

if __name__ == '__main__':
    # Parse arguments
    # Check if there are enough arguments
    if len(sys.argv) < 2:
        print("No command given!")
        usage()
        exit(1)
    else:
        check_path, runtime_path, latest_index = parse_arguments()

    files = {}
    if check_path == None:
        check_path = "./"
    # Generate the initial tree
    check_tree(check_path, files)
    while True:
        old_files = copy.deepcopy(files)
        time.sleep(1)
        check_tree(check_path, files)
        if resolve_changes(files, old_files):
            proc = subprocess.Popen(
                    sys.argv[latest_index + 1:], 
                    executable=sys.argv[latest_index],
                    cwd=runtime_path)
            retval = proc.wait()
            if retval != 0:
                print("Subprocess command failed!")
        


