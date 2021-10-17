#!/usr/bin/env python3
# Copyright 2021 Northwest Minzu University (siruiLi)
# Convert Tibetan words into phonemes
# usage: python3 labels.py --lexicon ./lexicon.txt  --phones ./corpus/file1/file1_phones.txt --transcript ./corpus/file1/file1_clean.txt
# This source code is licensed under the GNU Affero license found in the
# LICENSE file in the root directory of this source tree.


import argparse
import os

def get_parser():
    parser = argparse.ArgumentParser(
        description="Convert Tibetan words into phonemes"
    )
    parser.add_argument(
        "--lexicon",
        help="Tibetan lexicon text",
        default="lexicon.txt",
        required=True
    )
    parser.add_argument(
        "--words",
        help="Tibetan words text",
        default=None,
    )
    parser.add_argument(
        "--phones",
        help="Tibetan phones text",
        default="phones.txt",
        required=True
    )
    parser.add_argument(
        "--letters",
        help="Tibetan lexicon list",
        default = None,
    )
    parser.add_argument(
        "--transcript",
        help="Tibetan lexicon list",
        default="lexicon.lst",
        required=True
    )

    return parser

def process(lexicon, tran_file, phn_file, wrd_file = False, ltr_file = False):
    wrd_to_phn = {}
    with open(lexicon, "r", encoding='utf-8') as lf:
        for line in lf:
            items = line.rstrip().split(" ")
            assert len(items) > 1, line
            assert items[0] not in wrd_to_phn, items
            wrd_to_phn[items[0]] = items[1:]

    wrd_out = (
    open(wrd_file, "w", encoding='utf-8')
    if wrd_file
    else None
    )
    ltr_out = (
    open(ltr_file, "w", encoding='utf-8')
    if ltr_file
    else None
    )

    with open(phn_file, "w", encoding='utf-8') as phn_out, open(tran_file, "r", encoding='utf-8') as trans_f:
        words_texts = {}
        phones_texts = {}
        for tline in trans_f:
            items = tline.strip().split()
            words = []
            phones = []
            for w in items[1:]:
                if not (w in wrd_to_phn ):
                    continue
                else:
                    words.append(w)
                    phones.extend(wrd_to_phn[w])
            words_texts[items[0]] = " ".join(words)
            phones_texts[items[0]] = " ".join(phones)
        for key ,value in phones_texts.items():
            print(key,value, file=phn_out)
        for key ,value in words_texts.items():
            if wrd_out is not None:
                print(key,value, file=wrd_out)
            if ltr_out is not None:
                print(key," ".join(list(value.replace(" ", "|"))) + " |",
                file=ltr_out)


    if ltr_out is not None:
        ltr_out.close()
    if wrd_out is not None:
        wrd_out.close()



if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    lexicon = args.lexicon
    wrd_file = args.words
    ltr_file = args.letters
    phn_file = args.phones
    tran_file = args.transcript

    process(lexicon, tran_file, phn_file, wrd_file, ltr_file)
