#!/usr/local/bin/python3
__author__ = 'raccoon'

import re


def remove_table(content):
    table = re.compile("(┌(((─)+┬)+)(─)+┐)(.*?)└?((─+)┴)+(─+)┘", re.DOTALL)
    return table.sub('\n', content)
