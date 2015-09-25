import json
import urllib2
import pwd
import grp
import pickle
import re
import socket
import math
import inspect

from arkexport_tools.ret_code import *
from arkexport_tools.cifs_manager import CIFSManager
from ManageTools.exportmgr import Iscsi, Cifs, Nfs, get_public_ips
from ManageTools.util import debug


API_URL = "http://172.16.20.90:8108/cifs/namespace"

def test_add_namespace():
    debug.debug()
    url = API_URL + ""
    data = {
            'namespace': "test_ns"
    }
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data)).read()
    debug.debug(json.loads(response))
    
def test_del_namespace():
    debug.debug()
    url = API_URL + ""
    data = {
            'namespace': "test_ns"
    }
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req, json.dumps(data)).read()
    debug.debug(json.loads(response))

def test_add_link():
    debug.debug()
    url = API_URL + "/test_ns"
    data = {
            'ip': "172.16.20.93",
            'folder': "test_folder"
    }
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
#     req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req, json.dumps(data)).read()
    debug.debug(json.loads(response))
def test_del_link():
    debug.debug()
    url = API_URL + "/test_ns"
    data = {
            'folder': "test_folder"
    }
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req, json.dumps(data)).read()
    debug.debug(json.loads(response))

def test():
    debug.debug()
    try:
        action = "/shared_folders"
        url = "http://172.16.20.90:8108/cifs/shared_folders"
#         url = _restful_base + _cifs_base + action
        response = urllib2.urlopen(url).read()
        cifs_exports = json.loads(response)
        debug.debug(cifs_exports)
        for export in cifs_exports:
            pass
    except:
        cifs_exports = []
    

if __name__ == '__main__':
#     test()
#     test_del_namespace()
#     test_add_namespace()
#     test_add_link()
    test_del_link()
#     test_del_namespace()
    
    
    
