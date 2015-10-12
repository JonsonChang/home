import subprocess
import shutil
import os

VERSION = '3.5'
src_base = '/home/jonson/arkflex{version}/ax-managetools/src/'.format(version=VERSION)
dist_base = '/data/patch/usr/lib/python2.7/dist-packages'


def execvp(cmd):
    pos = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout_data, stderr_data) = pos.communicate()
    if pos.returncode != 0:
        return (False, stderr_data)
    else:
        return (True, stdout_data)

def rm_link(file):
    try:
        os.unlink(file)
    except:
        print "rm_link except:" + file 
        pass

def patch(src, dist):
    try:
        shutil.rmtree(dist)
    except:
        print "rmtree except:" + dist
        pass
    shutil.copytree(src, dist, symlinks=True)

src = os.path.join(src_base, "ManageTools")
dist = os.path.join(dist_base, "ManageTools")
patch(src, dist)

src = os.path.join(src_base, "arkexport_tools")
dist = os.path.join(dist_base, "arkexport_tools")
patch(src, dist)

src = os.path.join(src_base, "ManageServices")
dist = os.path.join(dist_base, "ManageServices")
patch(src, dist)

rm_link('/data/patch/usr/lib/python2.7/dist-packages/ManageTools/arkexport_tools')
rm_link('/data/patch/usr/lib/python2.7/dist-packages/ManageTools/ManageTools')


# patch web
src = os.path.join("/home/jonson/arkflex{version}/ax-backend/UI".format(version=VERSION))
dist = os.path.join("/data/patch/var/www/axui/")
patch(src, dist)
src = os.path.join("/home/jonson/arkflex{version}/ax-backend/UI/UI/static".format(version=VERSION))
dist = os.path.join("/data/web/static")
patch(src, dist)
rm_link('/data/patch/var/www/axui/arkexport_tools')
rm_link('/data/patch/var/www/axui/ManageTools')
# for current web env
os.system('cp -R /data/patch/var/www/axui/ /var/www/')
rm_link('/var/www/axui/arkexport_tools')
rm_link('/var/www/axui/ManageTools')
os.system('service apache2 restart')

# dfs upstart
src = '/home/jonson/arkflex{version}/ax-managetools/configuration/etc/init/hopebay-dfs.conf'.format(version=VERSION)
dist = '/etc/init/hopebay-dfs.conf'
shutil.copyfile(src, dist)


execvp('find /data/patch/usr/ -name "*.pyc" -exec rm -rf {} \;')
