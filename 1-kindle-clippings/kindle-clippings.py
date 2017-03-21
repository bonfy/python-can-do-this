# coding: utf-8

import os
import codecs

FOLDER_DIR = '/Volumes/Kindle/documents/'
CLIPPINGS_FILE = os.path.join(FOLDER_DIR, 'My Clippings.txt')

def _get_content():
    """ Get content from My Clippings.txt
    """
    assert os.path.exists(CLIPPINGS_FILE)
    with codecs.open(CLIPPINGS_FILE, encoding='utf-8') as f:
        content = f.read()
    return content

def _add_memo_to_file(memo, filename):
    """ Add memo to file
    :param memo string:     memo
    :param filename string: filename
    """
    if not os.path.exists(filename):
        with codecs.open(filename, mode='a', encoding='utf-8') as f:
            f.write('# {}\n\n'.format(filename[:-3]))
    with codecs.open(filename, mode='a', encoding='utf-8') as f:
        f.write('* {}\n'.format(memo))

def main():
    """ main
    step1: get content
    step2: split to memos with '==========\r\n'
    step3: each item add_memo_to_file
    """
    content = _get_content()
    memos = content.split('==========\r\n')
    for item in memos:
        i = item.split('\r\n')
        if len(i) > 2:
            filename = i[0] + '.md'
            memo = i[-2]
            _add_memo_to_file(memo, filename)

if __name__ == '__main__':
    main()
