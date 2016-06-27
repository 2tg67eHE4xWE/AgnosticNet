import ssl
import rinse
import urllib
import ssl
import os
import logging
import http
import requests


from rinse import client
from http.client import HTTPSConnection

class DEVCONN(object):
    def __init__(self, hostname, username='admin', password='admin',
                 debug=False, cachedir=None, verify=False, timeout=90, port=443):
        self._hostname = hostname
        self._username = username
        self._password = password
        self._port = port
        self._debug = debug
        self._cachedir = cachedir
        self._timeout = timeout

    def