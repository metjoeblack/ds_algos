

import re
import sys
import collections

def read_file_words(file_path):
    """
    statistics = {}
    ....
    statistics.setdefault(word, []).append(location)
    """
    WORD_RE = re.compile(r"\w+")

    statistics = collections.defaultdict()
    statistics.default_factory = list
    with open(file=file_path, mode="rt", encoding="utf-8") as fp:
        for line_no, line in enumerate(fp, start=1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                statistics[word].append(location)

    for key in sorted(statistics, key=str.upper):
        print(key, statistics[key])



class StrKeyDict(dict):

    def __contains__(self, key) -> bool:
        return key in self.keys() or str(key) in self.keys()

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default



def test_str_dict():
    d = StrKeyDict([("2", "two"), ("4", "four"), ("9", "nine")])
    print(d)

    print(d["4"])
    print(d[2])
    print(2 in d)
    print(1 in d)


# test_str_dict()



if __name__ == "__main__":
    # read_file_words("/home/shangguan/Downloads/test.txt")
    ...