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


class RisPort:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}:8443/realtimeservice2/services/RISService?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        self.history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[self.history])
        binding_name = '{http://schemas.cisco.com/ast/soap}RisBinding'
        service_addr = f'https://{hostname}:8443/realtimeservice2/services/RISService'
        self.service = self.client.create_service(binding_name, service_addr)

    def selectCmDevice(self, data):
        try:
            result = self.service.selectCmDevice(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def SelectCmDeviceExt(self, data):
        try:
            result = self.service.SelectCmDeviceExt(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def selectCtiItem(self, data):
        try:
            result = self.service.selectCtiItem(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def getServerInfo(self, data):
        try:
            result = self.service.getServerInfo(**data)
            return result
        except Exception as fault:
            self.last_exception = fault

    def SelectCmDeviceSIP(self, data):
        try:
            result = self.service.SelectCmDeviceSIP(**data)
            return result
        except Exception as fault:
            self.last_exception = fault
