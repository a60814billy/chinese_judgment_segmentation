#!/usr/local/bin/python3
__author__ = 'raccoon'

import re


def remove_eng_num(content):
    pattern = re.compile("[A-Za-z0-9\-\+\,]+", re.DOTALL)
    return pattern.sub('\n', content)
