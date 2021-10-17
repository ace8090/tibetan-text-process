#!/usr/bin/env python3
# Copyright 2021 Northwest Minzu University (siruiLi)
# Convert Tibetan words into phonemes
# usage: python tibetan_label.py --lexicon ./lexicon.txt --corpus ./corpus/
# This source code is licensed under the GNU Affero license found in the
# LICENSE file in the root directory of this source tree.

import os
import argparse

import transcript as tra
import labels as lab


def get_parser():
    parser = argparse.ArgumentParser(
        description = "Convert Tibetan text into phonemes"
    )
    parser.add_argument(
        "--lexicon",
        help = "Tibetan lexicon text",
        default = "./lexicon.txt",
        required = True
    )
    parser.add_argument(
        "--corpus",
        help = "Tibetan corpus folder",
        default = "./corpus",
        required = True
    )
    parser.add_argument(
        "--words",
        help = "Tibetan words text",
        default = False,
    )
    parser.add_argument(
        "--letters",
        help = "Tibetan letters text",
        default = False,
    )

    return parser

def main(lexicon, corpus, wrd_file, ltr_file):
    for root, dirs, files in os.walk(corpus):
        for dir in dirs:
            source = os.path.join(root, dir, dir+".txt")
            tran_file = os.path.join(root, dir, dir+"_clean.txt")
            phn_file = os.path.join(root, dir, dir+"_phones.txt")
            if wrd_file:
                wrd_file = os.path.join(root, dir, dir+"_words.txt")
            if ltr_file:
                ltr_file = os.path.join(root, dir, dir+"_letters.txt")

            tra.pre_process(source, tran_file)
            lab.process(lexicon, tran_file, phn_file, wrd_file, ltr_file)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    lexicon = args.lexicon
    wrd_file = args.words
    ltr_file = args.letters
    corpus = args.corpus

    main(lexicon, corpus, wrd_file, ltr_file)
            