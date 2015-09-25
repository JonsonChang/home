import subprocess
import shutil
import os

src_base = '/home/jonson/ax-managetools/src/'
dist_base = '/data/patch/usr/lib/python2.7/dist-packages'


def execvp(cmd):
    pos = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout_data, stderr_data) = pos.communicate()
    if pos.returncode != 0:
        return (False, stderr_data)
    else:
        return (True, stdout_data)

def patch(src, dist):
	try:
		shutil.rmtree(dist)
	except:
		pass
	shutil.copytree(src,dist,symlinks=True)

src = os.path.join(src_base, "ManageTools") 
dist = os.path.join(dist_base, "ManageTools") 
patch(src, dist)

src = os.path.join(src_base, "arkexport_tools") 
dist = os.path.join(dist_base, "arkexport_tools") 
patch(src, dist)

src = os.path.join(src_base, "ManageServices") 
dist = os.path.join(dist_base, "ManageServices") 
patch(src, dist)

os.unlink('/data/patch/usr/lib/python2.7/dist-packages/ManageTools/arkexport_tools')
os.unlink('/data/patch/usr/lib/python2.7/dist-packages/ManageTools/ManageTools')


src = '/home/jonson/ax-managetools/configuration/etc/init/hopebay-dfs.conf'
dist = '/etc/init/hopebay-dfs.conf'
shutil.copyfile(src,dist)


execvp('find /data/patch/usr/ -name "*.pyc" -exec rm -rf {} \;')