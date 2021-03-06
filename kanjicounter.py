__author__ = 'sm4'

import collections

import xml.etree.cElementTree as ET
import unicodedata


class KanjiCounter:
    def __init__(self):
        pass

    def parse(self, source, tag):
        counter = collections.Counter()
        index = 0
        for event, elem in ET.iterparse(source, events=("start", "end")):
            if event == "end":
                if elem.tag == tag:
                    for x in str(elem.text):
                        try:
                            if unicodedata.name(x).startswith("CJK UNIFIED IDEOGRAPH"):
                                counter.update(x)
                        except ValueError:
                            pass
                    index += 1
                    if index % 100 == 0:
                        print("Progress: " + str(index))
                elem.clear()
        return counter