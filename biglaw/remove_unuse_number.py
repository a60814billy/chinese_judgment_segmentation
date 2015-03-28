#!/usr/local/bin/python3
__author__ = 'raccoon'

import re


def remove_unuse_number(content):
    pattern = re.compile("(\d{2,3}\s*年度.*?字第\s*\d+\s*號)|(第\s*\d+-?\d*\s*(條|段|項|款)(之\d+)?)|((中\s*華\s*民\s*國\s*)?(民\s*國\s*)?\d+\s*年\s*\d+\s*月\s*\d+\s*日)|(\d{4,})|([A-Z]\d+\W*號)|(\d{3,}-\d{3,}號?)|((○|0)+(區|街|巷|號|路|段|弄))", re.DOTALL)
    return pattern.sub('\n', content)
