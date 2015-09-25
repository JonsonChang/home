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

def PrintDebug(msg=""):
  callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  #print info.filename                       # __FILE__     -> Test.py
  #print info.function                       # __FUNCTION__ -> Main
  #print info.lineno                         # __LINE__     -> 13
  print '{0} {1}({2}): {3}'.format(info.filename, info.function,info.lineno,msg)

  
def test()  :
    PrintDebug()
    PrintDebug()

if __name__ == '__main__':
    PrintDebug()
    ns = "dfs"
    cifs_mgr = CIFSManager()

#     settings = {
#                 "host msdfs": "yes",
# #                 "netbios name" : "GMYNADEF",
#             }    
#     if cifs_mgr.set_global_settings(settings) != OP_SUCCESS:
#         raise Exception("Unable to update settings")
        
    cifs_mgr.remove_share(ns,True)
    
    ret = cifs_mgr.create_namespace(ns)
    if ret != CIFS_CREATE_SUCCESS:
        print "[Error] cifs_mgr.create_namespace return code: {0}".format(ret)
        
        
    ret = cifs_mgr.add_namespace_link(ns, '172.16.20.92', 'cifs_2')
    if  ret != CIFS_CREATE_SUCCESS:
        print "[Error] cifs_mgr.add_namespace_link return code: {0}".format(ret)
         
    
    
    ret = cifs_mgr.add_namespace_link(ns, '172.16.20.92', 'cifs_2')
    if  ret != CIFS_CREATE_SUCCESS:
        print "[Error] cifs_mgr.add_namespace_link return code: {0}".format(ret)
         
    ret = cifs_mgr.add_namespace_link(ns, '172.16.20.92', 'cifs_23')
    if  ret != CIFS_CREATE_SUCCESS:
        print "[Error] cifs_mgr.add_namespace_link return code: {0}".format(ret)
         
    ret = cifs_mgr.add_namespace_link(ns, '172.16.20.92', 'cifs_24')
    if  ret != CIFS_CREATE_SUCCESS:
        print "[Error] cifs_mgr.add_namespace_link return code: {0}".format(ret)
         
#     
    
    debug.info("b")
    
#     cifs_mgr.restart_service()
    PrintDebug("done")
