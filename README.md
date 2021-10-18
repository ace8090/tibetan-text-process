# Tibetan text process

Convert Tibetan text into phonemes

## Instruction

Using this tool, you can clean Tibetan text, remove Chinese and English symbols and special symbols, convert Tibetan text into phoneme labels, and generate words and letters labels with more parameter options.

A sample corpus folder is given in this project. Please change the corresponding corpus folder path for formal use.

Usage: the following scripts are run using Python3

```sh
python tibetan_label.py --lexicon ./lexicon.txt --corpus ./corpus/

# The phoneme transcription of the corresponding text is generated in the subfolder of corpus
```

Parameter description

|parameter|illustration|default|required|
|--|--|--|--|
|--lexicon|Lexicon file path|./lexicon.txt|True|
|--corpus|Corpus folder path|./corpus/|True|
|--words|Generate words annotation|False|False|
|--letters|Generate letters annotation|False|False|

If you want to generate phones, words and letters labels at the same time, please use the following command

```
python tibetan_label.py --lexicon ./lexicon.txt --corpus ./corpus/ --words True --letters True
```

## Additional features

The transcript.py script can clean up a single Tibetan text

```
python transcript.py --source_file ./corpus/file1/file1.txt --target_file ./corpus/file1/file1_clean.txt
```

The labels.py script can phonemize a single Tibetan text

```
python3 labels.py --lexicon ./lexicon.txt  --phones ./corpus/file1/file1_phones.txt --transcript ./corpus/file1/file1_clean.txt
```

## License

This project is licensed under the GNU Affero license.

Please indicate the source, do not use for commercial purposes.
