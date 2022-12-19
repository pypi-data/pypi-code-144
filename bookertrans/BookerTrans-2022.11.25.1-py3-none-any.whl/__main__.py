# coding: utf-8

import os
from os import path
from argparse import ArgumentParser
import threading
import traceback
import copy
from concurrent.futures import ThreadPoolExecutor
from . import trans_html, __version__
from .apis import apis
from .config import config

trlocal = threading.local()

is_html = lambda f: f.endswith('.html') or \
                    f.endswith('.htm') or \
                    f.endswith('.xhtml')

def process_file_safe(args):
    try: process_file(args)
    except: traceback.print_exc()

def process_file(args):
    fname = args.fname
    if not is_html(fname):
        print(f'{fname} is not a html file')
        return
        
    if not hasattr(trlocal, 'api'):
        trlocal.api = load_api(args)
    api = trlocal.api
    
    print(fname)
    html = open(fname, encoding='utf-8').read()
    html = trans_html(api, html)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

def process_dir(args):
    dir = args.fname
    files = [f for f in os.listdir(dir) if is_html(f)]
    pool = ThreadPoolExecutor(args.threads)
    hdls = []
    for f in files:
        f = path.join(dir, f)
        args = copy.deepcopy(args)
        args.fname = f
        # process_file_safe(args)
        h = pool.submit(process_file_safe, args)
        hdls.append(h)
    for h in hdls: h.result()

def load_api(args):
    api = apis[args.site]()
    api.host = args.host
    api.proxy = args.proxy
    api.timeout = args.timeout
    return api

def main():
    parser = ArgumentParser(prog="BookerTrans", description="HTML Translator with Google Api for iBooker/ApacheCN")
    parser.add_argument('site', help='translate api', choices=apis.keys())
    parser.add_argument('fname', help="html file name or dir name")
    parser.add_argument('-v', '--version', action="version", version=__version__)
    parser.add_argument('-H', '--host', default='translate.google.cn', help="host for google translator")
    parser.add_argument('-P', '--proxy', help=f'proxy with format \d+\.\d+\.\d+\.\d+:\d+ or empty')
    parser.add_argument('-T', '--timeout', type=float, help=f'timeout in second')
    parser.add_argument('-t', '--threads', type=int, default=8, help=f'num of threads')
    parser.add_argument('-w', '--wait-sec', type=float, default=1.5, help='delay in second between two times of translation')
    parser.add_argument('-r', '--retry', type=int, default=10, help='count of retrying')
    parser.add_argument('-s', '--src', default='auto', help='src language')
    parser.add_argument('-d', '--dst', default='zh-CN', help='dest language')
    parser.add_argument('-D', '--debug', action='store_true', help='debug mode')
    args = parser.parse_args()
    
    if args.proxy:
        p = args.proxy
        args.proxy = {'http': p, 'https': p}
    
    config['wait_sec'] = args.wait_sec
    config['retry'] = args.retry
    config['src'] = args.src
    config['dst'] = args.dst
    config['debug'] = args.debug

    if path.isdir(args.fname):
        process_dir(args)
    else:
        process_file(args)
        
if __name__ == '__main__': main()
