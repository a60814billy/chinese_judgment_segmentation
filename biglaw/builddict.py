__author__ = 'raccoon'

import re
from .wordcount import WordCount
from .remove_table import remove_table
from .remove_unuse_number import remove_unuse_number
from .remove_eng_num import remove_eng_num

class BuildDict:
    wc = WordCount()
    n_word = 8

    def add_index(self, content):
        contents = remove_eng_num(remove_unuse_number(remove_table(content))).split('\n')
        for i in contents:
            split_content = re.split("。|：|；|（|）|「|」|，|、|】|【|\(|\)", i)
            for sc in split_content:
                for j in range(len(sc)):
                    for k in range(2, self.n_word + 1):
                        self.wc.push(sc[j:j + k])

    def output(self):
        return self.wc.get_dict()