__author__ = 'Melvin Douglas'
__version__ = '12'
__email__ = 'melvin.douglas@hotmail.com'
__status__ = 'Production'
# https://d1nmyq4gcgsfi5.cloudfront.net/site/sxml/documents/api-reference/service-control/

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


class ControlCenterServicesExPort:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}:8443/controlcenterservice2/services/ControlCenterServicesEx?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])
        binding_name = '{http://schemas.cisco.com/ast/soap}ControlCenterServicesExBinding'
        service_addr = f'https://{hostname}:8443/controlcenterservice2/services/ControlCenterServicesEx'
        self.service = self.client.create_service(binding_name, service_addr)

    def getStaticServiceListExtended(self, data, serialize=False):
        try:
            result = self.service.getStaticServiceListExtended(data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if serialize is True:
            return serialize_object(result)
        return result

    def getFileDirectoryList(self, data, serialize=False):
        try:
            result = self.service.getFileDirectoryList(data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if serialize is True:
            return serialize_object(result)
        return result

    def soapDoServiceDeploymentNoDbUpdate(self, data, serialize=False):
        try:
            result = self.service.soapDoServiceDeploymentNoDbUpdate(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if serialize is True:
            return serialize_object(result)
        return result

    def soapDoControlServicesEx(self, data, serialize=False):
        try:
            result = self.service.soapDoControlServicesEx(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if serialize is True:
            return serialize_object(result)
        return result
