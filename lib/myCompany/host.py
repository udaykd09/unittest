import logging
import os
#import paramiko
import re
import socket  # gethostbyname
import subprocess  # Popen, PIPE
import sys


class BaseHost(object):
    def __init__(self, hostname, **kwargs):
        pass

    @property
    def ip(self):
        pass

    @property
    def location(self):
        if hasattr(self, 'user'):
            return "{0}@{1}".format(self.user, self.hostname)
        else:
            return self.hostname

    def __str__(self):
        cls_name = self.__class__.__name__
        return '<%s %s>' % (cls_name, self.location)

    def __repr__(self):
        cls_name = self.__class__.__name__
        return "<%s %s at 0x%x>" % (cls_name, self.location, id(self))


class Host(BaseHost):
    def __init__(self, hostname, user, passwd):
        pass

    def ssh_cmd(self):
        pass

    def scp_cmd(self):
        pass

    def run_cmd(self):
        pass


class LocalHost(Host):
    # Handle 127.0.0.1 or localhost equivalently
    def __init__(self, **kwargs):
        Host.__init__(self, 'localhost', **kwargs)


class ProxyHost(Host):
    def __init__(self, hostname, proxy_hostname):
        pass
