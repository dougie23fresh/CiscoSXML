__author__ = 'Melvin Douglas'
__version__ = '12'
__email__ = 'melvin.douglas@hotmail.com'
__status__ = 'Production'

import os
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from zeep.helpers import serialize_object
from requests import Session
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

disable_warnings(InsecureRequestWarning)

class PerfmonPort:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}/perfmonservice/services/PerfmonPort?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])

    def PerfmonOpenSession(self):
        try:
            result = self.client.service.PerfmonOpenSession()
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonAddCounter(self, data):
        try:
            result = self.client.service.PerfmonAddCounter(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonRemoveCounter(self, data):
        try:
            result = self.client.service.PerfmonRemoveCounter()
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonCollectSessionData(self, data):
        try:
            result = self.client.service.PerfmonCollectSessionData(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonCloseSession(self, data):
        try:
            result = self.client.service.PerfmonCloseSession(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonListInstance(self, data):
        try:
            result = self.client.service.PerfmonListInstance(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonQueryCounterDescription(self, data):
        try:
            result = self.client.service.PerfmonQueryCounterDescription(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonListCounter(self, data):
        try:
            result = self.client.service.PerfmonListCounter()
            return result
        except Exception as fault:
            self.last_exception = fault

    def PerfmonCollectCounterData(self):
        try:
            result = self.client.service.PerfmonCollectCounterData()
            return result
        except Exception as fault:
            self.last_exception = fault
