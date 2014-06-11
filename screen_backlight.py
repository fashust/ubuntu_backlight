#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    control screen backlight
"""
from __future__ import print_function, absolute_import
import re
import argparse
import subprocess


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmeil.com'


parser = argparse.ArgumentParser(description='Controll screen backlight.')
parser.add_argument('--controll', type=str, default='up')
args = parser.parse_args()


STEP = 25
COMMAND = "/usr/bin/sudo /usr/bin/intel_backlight {}"


def up(current):
    """
        increase
        :param current:
    """
    print(current)
    return current + STEP if current != 100 else current


def down(current):
    """
        decrease
        :param current:
    """
    print(current)
    return current - STEP if current else current


def set_bright(val):
    """
        set bright value
    """
    subprocess.Popen(
        COMMAND.format(val),
        stdout=subprocess.PIPE,
        shell=True
    ).stdout.read()


def main():
    """
        main
    """
    directions = {
        'up': up,
        'down': down
    }
    a = subprocess.Popen(
        COMMAND.format(''),
        stdout=subprocess.PIPE,
        shell=True
    ).stdout.read()
    val = directions.get(
        args.controll, 'up'
    )(int(re.findall(r'\d+', a)[0]))
    set_bright(val)
    print(val)


if __name__ == '__main__':
    main()
