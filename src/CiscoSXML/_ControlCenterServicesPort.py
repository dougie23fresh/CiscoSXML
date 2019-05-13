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
import urllib3

class ControlCenterServicesPort:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}/controlcenterservice/services/ControlCenterServicesPort?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])
    def list_services(self):
        values = []
        for service in self.client.wsdl.services.values():
            print("service:", service.name)
            for port in service.ports.values():
                values.append(port.binding._operations.values())
        return values
    def _callSoap_func(self, func_name, data, serialize=False):
        try:
            result = getattr(self.client.service, func_name)(**data)
            #result = self.service.updateAppUser(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if result is not None: result = result['return']
        if serialize is True:
            return serialize_object(result)
        return result
    def soapGetStaticServiceList(self, data, serialize=False):
        return self._callSoap_func('soapGetStaticServiceList', data, serialize)
    def soapGetServiceStatus(self, data, serialize=False):
        return self._callSoap_func('soapGetServiceStatus', data, serialize)
    def soapDoServiceDeployment(self, data, serialize=False):
        return self._callSoap_func('soapDoServiceDeployment', data, serialize)
    def soapDoControlServices(self, data, serialize=False):
        return self._callSoap_func('soapDoControlServices', data, serialize)
    def getProductInformationList(self, data, serialize=False):
        return self._callSoap_func('getProductInformationList', data, serialize)
