#!/usr/bin/env python3
from plexarr.utils import get_py_path
from configparser import ConfigParser
from bottle import template
from pathlib import Path
from furl import furl
from rich import print
import argparse
import sys


base_path = get_py_path()
def configSetup(iptv='lemo2'):
    config = ConfigParser()
    config.read(Path.home().joinpath('.config', 'plexarr.ini'))
    dns_url = furl(config[iptv].get('api_url')).origin
    username = config[iptv].get('username')
    password = config[iptv].get('password')

    # -- generate config.js        
    config_js = base_path.joinpath('public', 'config.js')
    tpl = template('config_js.tpl', dns_url=dns_url)
    #print(tpl)
    config_js.write_text(tpl)

    # -- generate config.php
    config_php = base_path.joinpath('public', 'config.php')
    tpl = template('config_php.tpl', iptv=iptv, dns_url=dns_url, username=username, password=password)
    #print(tpl)
    config_php.write_text(tpl)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("iptv", default="lemo2", help="IPTV to setup the configs with")
    args = ap.parse_args()
    configSetup(iptv=args.iptv)

if __name__ == "__main__":
    sys.exit(main())
