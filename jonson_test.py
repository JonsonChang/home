import json
import urllib2
import pwd
import grp
import pickle
import re
import socket
import math
import inspect

from ManageTools.exportmgr import Iscsi, Cifs, Nfs, get_public_ips

def PrintDebug():
  callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  #print info.filename                       # __FILE__     -> Test.py
  #print info.function                       # __FUNCTION__ -> Main
  #print info.lineno                         # __LINE__     -> 13
  print '{0} {1}({2})'.format(info.filename, info.function,info.lineno)

  
def test()  :
    PrintDebug()
    PrintDebug()

if __name__ == '__main__':
    PrintDebug()
    cifs = Cifs()
#     cifs.namespace_create("name space")
    print cifs.namespace_list()