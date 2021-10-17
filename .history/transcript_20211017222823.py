#! /usr/bin/env python3
# Copyright 2021 Northwest Minzu University (siruiLi senyanLi)
# Dealing with Chinese and English symbols and special symbols in Tibetan
# usage: python transcript.py --source_file ./corpus/file1/file1.txt --target_file ./corpus/file1/file1_clean.txt
# This source code is licensed under the GNU Affero license found in the
# LICENSE file in the root directory of this source tree.

import argparse
import re

def get_parser():
    parser = argparse.ArgumentParser(
        description="Tibetan text clean"
    )
    parser.add_argument(
        "--source_file",
        help="Original Tibetan text",
        default="sentence.txt",
        required=True
    )
    parser.add_argument(
        "--target_file",
        help="Clean Tibetan text",
        default="sentence_clean.txt",
        required=True
    )

    return parser


def pre_process(source, target):
    #The characters to be deleted are added to the punctuation
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”？，！．〈〉〔〕–【】（）、。：；’‘……￥《》——·追思ⅡⅧ①⑥⑦②何须事无细皆躬亲碍爱°Ⅰ㎝～༠﻿③"""
    with open(source, 'r') as f_source,open(target, 'w') as f_target:
        for line in f_source:
            items = line.strip().split()
            text = " ".join(items[1:])
            words = re.findall('[0-9\uFF10-\uFF19a-zA-Z]+[\']?[-]?[0-9\uFF10-\uFF19a-zA-Z]*',text)
            for word in words:
                text = text.replace(word,'་'+word+'་')
            for i in punctuation:
                text = text.replace(i, '་')
            text = text.replace('།','་')
            text = text.replace('་', ' ')
            print(items[0]," ".join(text.split()), file=f_target)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    source = args.source_file
    target = args.target_file

    pre_process(source, target)



    
