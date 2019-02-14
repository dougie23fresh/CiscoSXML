__author__ = 'Melvin Douglas'
__copyright__ = 'Copyright 2018, Melvin Douglas'
__credits__ = []
__license__ = 'MIT'
__version__ = '1'
__maintainer__ = 'Melvin Douglas'
__email__ = 'melvin.douglas@'
__status__ = 'Development' #'Prototype', 'Development', or 'Production'.

from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from requests import Session
from requests.auth import HTTPBasicAuth
import urllib3

# allow program to continue running without
# warnings about not verifying HTTPS certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Allow DH ciphers
urllib3.util.ssl_.DEFAULT_CIPHERS = 'HIGH:!DH:!aNULL' #= 'ALL'

class perfmonport:
    def __init__(self, username, password, server_ip, tls_verify=True, timeout=10):
        self.last_exception = None

        wsdl = f'https://{server_ip}/perfmonservice/services/PerfmonPort?wsdl'

        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)

        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])
        
    def functions(self):
        for service in self.client.wsdl.services.values():
            print("service:", service.name)
            for port in service.ports.values():
        
                print(port.binding._operations.values())

    def PerfmonOpenSession(self):
        try:
            result = self.client.service.PerfmonOpenSession()
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonAddCounter(self, perfmon_session, list_of_counters):
        try:
            result = self.client.service.PerfmonAddCounter(SessionHandle=perfmon_session, ArrayOfCounter=list_of_counters)
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonRemoveCounter(self):
        try:
            result = self.client.service.PerfmonRemoveCounter()
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonCollectSessionData(self, perfmon_session):
        try:
            result = self.client.service.PerfmonCollectSessionData(SessionHandle=perfmon_session)
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonCloseSession(self, perfmon_session):
        try:
            result = self.client.service.PerfmonCloseSession(SessionHandle=perfmon_session)
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonListInstance(self, host, perfmon_object):
        try:
            result = self.client.service.PerfmonListInstance(Host=host, Object=perfmon_object)
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonQueryCounterDescription(self):
        try:
            result = self.client.service.PerfmonQueryCounterDescription()
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonListCounter(self, host):
        try:
            result = self.client.service.PerfmonListCounter(Host=host)
        except Exception as fault:
            self.last_exception = fault
        return result
    
    def PerfmonCollectCounterData(self):
        try:
            result = self.client.service.PerfmonCollectCounterData()
        except Exception as fault:
            self.last_exception = fault
        return result
