
import sys
import time
import paramiko
import cmd


class Server:
    client = None
    host = ''
    port = 22
    conn_user = None
    conn_passwd = None
    conn_stat = 0

    def __init__(self, host='', port=22, user=None, passwd=None):
        self.setconn(host, port, user, passwd)

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.reconnect()

    def __del__(self):
        if self.conn_stat == 1:
            self.client.close()

    def setconn(self, host='', port=22, user=None, passwd=None):
        self.host = host
        self.port = port
        self.conn_user = user
        self.conn_passwd = passwd

    def reconnect(self):
        if self.conn_stat == 1:
            self.client.close()
            self.conn_stat = 0
        try:
            self.client.connect(self.host, self.port, self.conn_user, self.conn_passwd)
            self.conn_stat = 1
        except:
            print 'Unable connect to %s' % self.host

    def show(self, result):
        for i in range(0, len(result)):
            print result[i]

    def run(self, cmd=None, echo='Y', out='N', err='N'):
        if self.conn_stat == 0:
            raise 'connect state error'
        if echo == 'Y':
            print cmd
        # start
        stdin, stdout, stderr = self.client.exec_command(cmd)
        # result
        if out == 'Y':
            # print 'stdout:'
            self.show(stdout.readlines())
        if err == 'Y':
            # print 'stderr:'
            self.show(stderr.readlines())
        # exit
        stdin.close()
        stdout.close()
        stderr.close()


def main(argv, argc):
    ssh1 = Server('172.16.20.90', 22, 'hopebayadmin', 'njo61u04')
    ssh2 = Server('172.16.20.91', 22, 'hopebayadmin', 'njo61u04')
    ssh3 = Server('172.16.20.92', 22, 'hopebayadmin', 'njo61u04')
    ssh4 = Server('172.16.20.93', 22, 'hopebayadmin', 'njo61u04')

    ssh1.run("rm -rf /data/patch")
    ssh2.run("rm -rf /data/patch")
    ssh3.run("rm -rf /data/patch")
    ssh4.run("rm -rf /data/patch")

    commands = ["cp /etc/iscsi/initiatorname.iscsi /tmp",
                "stop winbind",
                "umount /etc",
                "rm -rf /conf/etc/*",
                "rm -f /conf/flags/PRE_INITIALIZED",
                "rm -rf /conf/.etc",
                "mkdir /conf/.etc",
                "cp -Rp /usr/local/reset/* /conf",
                "chown -R www-data:www-data /conf/flags",
                "rm -f /conf/flags/ZFS_UNCONFIG",
                "mkdir -p /conf/etc/iscsi",
                "copy /tmp/initiatorname.iscsi /conf/etc/iscsi/"]

    for cmd in commands:
        ssh1.run(cmd)
        ssh2.run(cmd)
        ssh3.run(cmd)
        ssh4.run(cmd)

    ssh1.run("echo -n 0 0 > /conf/conf/nodeinfo.conf")
    ssh2.run("echo -n 0 1 > /conf/conf/nodeinfo.conf")
    ssh3.run("echo -n 0 2 > /conf/conf/nodeinfo.conf")
    ssh4.run("echo -n 0 3 > /conf/conf/nodeinfo.conf")

    ssh1.run("echo -n 4 A I B B > /conf/conf/int_type.conf")
    ssh2.run("echo -n 4 A I B B > /conf/conf/int_type.conf")
    ssh3.run("echo -n 4 A I B B > /conf/conf/int_type.conf")
    ssh4.run("echo -n 4 A I B B > /conf/conf/int_type.conf")

    ssh1.run("echo -n 2 > /conf/conf/ssdcache.conf")
    ssh2.run("echo -n 2 > /conf/conf/ssdcache.conf")
    ssh3.run("echo -n 2 > /conf/conf/ssdcache.conf")
    ssh4.run("echo -n 2 > /conf/conf/ssdcache.conf")

    ssh1.run("echo -n 172.16.20.90 255.255.255.0 172.16.20.254 168.95.1.1 > /conf/conf/usernet.conf")
    ssh2.run("echo -n 172.16.20.91 255.255.255.0 172.16.20.254 168.95.1.1 > /conf/conf/usernet.conf")
    ssh3.run("echo -n 172.16.20.92 255.255.255.0 172.16.20.254 168.95.1.1 > /conf/conf/usernet.conf")
    ssh4.run("echo -n 172.16.20.93 255.255.255.0 172.16.20.254 168.95.1.1 > /conf/conf/usernet.conf")

    ssh1.run("timeout 30 sync; ipmi-chassis --chassis-control=POWER-DOWN")
    ssh2.run("timeout 30 sync; ipmi-chassis --chassis-control=POWER-DOWN")
    ssh3.run("timeout 30 sync; ipmi-chassis --chassis-control=POWER-DOWN")
    ssh4.run("timeout 30 sync; ipmi-chassis --chassis-control=POWER-DOWN")

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
