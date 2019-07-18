## MacOS SET PROXY

### 缘起

有时候在工作的时候经常要切换代理（实在也是因为两个工作地点，一个可以用自己的代理，一个只能用公司的代理），所以写个脚本自动切换成公司代理。

备注： 自己的代理是用工具的，工具会帮你切，公司的代理只能手填

### 使用

```command
$ export WORK_PROXY=localhost
$ export WORK_PORT=8080
$ python3 set-macos-proxy.py on # or off
```

当然不想费事的 直接将文件中的 WORK_PROXY 与 WORK_PORT 赋值成自己的设置就行了

### 分析

使用 `networksetup` 这个命令就可以了 

主要用到了

```command
$ networksetup -setwebproxy Wi-Fi proxy port
$ networksetup -setsecurewebproxy Wi-Fi proxy port
$ networksetup -setsocksfirewallproxy Wi-Fi proxy port

$ networksetup -setwebproxystate Wi-Fi on
$ networksetup -setsecurewebproxystate Wi-Fi on
$ networksetup -setsocksfirewallproxystate Wi-Fi on
```

注意 这个 `Wi-Fi` 是你的网络名称

可以用下面这两个命令查看

```command
$ networksetup -listallnetworkservices
$ networksetup -listnetworkserviceorder
```

### 代码

```python
# coding: utf-8

import os
import sys

PROXY = os.getenv('WORK_PROXY', 'localhost')
PORT = os.getenv('WORK_PORT', 8080)
NET = 'Wi-Fi'
TYPS = ['web', 'secureweb', 'socksfirewall']

def proxy_setting(proxy, port):
    # Set proxy
    for w in TYPS:
        cmd = f'networksetup -set{w}proxy {NET} {proxy} {port}'
        print(cmd)
        os.system(cmd)

def proxy_switch(key='off'):
    # Turn proxy on or off
    for w in TYPS:
        cmd = f'networksetup -set{w}proxystate {NET} {key}'
        print(cmd)
        os.system(cmd)

def proxy_on(proxy=PROXY, port=PORT):
    proxy_setting(proxy, port)
    proxy_switch('on')

def proxy_off():
    proxy_setting('localhost', 0)
    proxy_switch('off')

if __name__ == '__main__':
    cmd_length = len(sys.argv)
    if (cmd_length != 2):
        print('Usage: python3 set-macos-proxy.py on # or off')
        sys.exit(0)

    param = sys.argv[1]

    if param == 'on':
        proxy_on()
    elif param == 'off':
        proxy_off()
    else:
        print('Usage: python3 set-macos-proxy.py on # or off')

```

### 参考

* https://gist.github.com/jordelver/3073101
* https://stackoverflow.com/questions/39904647/how-to-set-proxy-settings-on-macos-using-python