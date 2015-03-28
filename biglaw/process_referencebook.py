__author__ = 'raccoon'


class RefProcess:
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        f = open(self.filename)
        content = f.read()
        content_without_space = content.replace(" ", "").replace("　", "")
        paragraphs = content_without_space.split('\n')
        content = content.split('\n')

        paragraph_mark = []

        output = ""

        symbol = ["，", "。", "、", "（", "）", "：", "，", "」", "「", "-", "─", "┼", "┌", "┬"]

        for i in range(len(paragraphs)):
            is_paragraph = False
            for j in range(len(symbol)):
                if paragraphs[i].find(symbol[j]) >= 0:
                    is_paragraph = True
                    break
            if not is_paragraph:
                if len(paragraphs[i]) > 10:
                    is_paragraph = True
            paragraph_mark.append(is_paragraph)

        for i in range(len(paragraph_mark)):
            if i + 1 < len(paragraph_mark):
                if not paragraph_mark[i]:
                    output += paragraphs[i] + '\n'
                elif paragraph_mark[i + 1]:
                    output += paragraphs[i]
                else:
                    output += paragraphs[i] + '\n'
            else:
                output += paragraphs[i] + '\n'
        return output