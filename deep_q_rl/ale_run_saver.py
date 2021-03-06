""" This script runs a pre-trained network with the game
visualization turned on.

Usage:

ale_run_watch.py NETWORK_PKL_FILE [ ROM ]
"""
import subprocess
import sys

def run_save(display_screen=True):
    command = ['./run_nature_saver.py', '--steps-per-epoch', '0', '--nn-file', sys.argv[1]]

    if display_screen :
        command.extend(['--display-screen'])
    if len(sys.argv) > 2:
        command.extend(['--rom', sys.argv[2]])
    if len(sys.argv) > 3:
        command.extend(['--epochs', sys.argv[3]])
    
    if len(sys.argv) > 4:
        command.extend(['--out_file', sys.argv[4]])
    if len(sys.argv) > 5:
        command.extend(['--test-length', sys.argv[5]])
    else :
        command.extend(['--test-length', ' 10000'])

    p1 = subprocess.Popen(command)
    
    p1.wait()

if __name__ == "__main__":
    run_save(False)
