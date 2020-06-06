from xmlrpclib import ServerProxy
from os.path import join, isfile
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import sys

MAX_HISTORY_LENGTH = 4
OK = 1
FAIL = 2
EMPTY = ''


def getPort(url):
    name = urlparse(url):[1]
    parts = name.split(':')
    return int(parts[-1])


class Node:

    def __init__(self, url, dirname, secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set()


    def query(self, query):

