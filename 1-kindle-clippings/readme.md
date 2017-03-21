## Kindle Clippings

### 缘起

刚入手一个kindle,一直在上面看书，并坚持写小结，里面需要把kindle里面的批注写进自己的小结里面备忘，本来是用的Knote,其实还蛮好用的，但只有7天的试用期，**又不想花钱**，算了看了下kindle 下面批注的文件 `My Clippings.txt`好像结构也不是太复杂，就自己写个脚本。

### 目标

读取 kindle 里的`My Clippings.txt`，将其每本书的批注导出，存入`书名.md`

### 分析

其实 这里可以用 ipython 先试着写下，看看结构

![图一](http://bonfy.qiniudn.com/kindle-1.png)
![图二](http://bonfy.qiniudn.com/kindle-2.png)

分析出分割符 "==========\r\n"

![图三](http://bonfy.qiniudn.com/kindle-3.png)

分析出用 "\r\n" 进行分隔后 第一项为 书名， 倒数第二项为 备注

### 完整代码

其实代码不长，简单的IO读写

```python
# coding: utf-8

import os
import codecs

FOLDER_DIR = '/Volumes/Kindle/documents/' # MAC下的文件夹地址
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

```

## 实现结果

![图四](http://bonfy.qiniudn.com/kindle-4.png)

## 友情提醒

1. 请记得先把Kindle连上电脑
2. 此程序在mac下面能够正常运行，Windows下面请修改 `FOLDER_DIR`
3. 导出来的 markdown 文件建议 copy 导其他文件夹再编辑，一面辛辛苦苦地排版半天，下次导出又全部覆盖掉，别说我没提醒你哦
