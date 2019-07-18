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