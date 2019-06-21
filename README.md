# Python Wrapper for Cisco UC Serviceability XML API (SXML)

This is a Python based wapper fo the Unified CM SXML API

## RisPort (Real Time Information Port) SOAP Service

```python
import CiscoSXML as sxml
c = sxml.RisPort70(USERNAME, PASSWORD, HOSTNAME, tls_verify=False)
ex = {
    'StateInfo': '',
    'CmSelectionCriteria': {
        'MaxReturnedDevices': '10',
        'DeviceClass': 'Phone',
        'Model': '255',
        'Status': 'Any',
        'NodeName': '',
        'SelectBy': 'DirNumber',
        'SelectItems': {
            'item': [
                '11111',
            ]
        },
        'Protocol': 'Any',
        'DownloadStatus': 'Any'
    }
}
print(c.selectCmDevice(ex))
print(c.selectCmDeviceExt(ex))
```

## PerfmonPort (Performance Information Port) SOAP Service

```python
import CiscoSXML as sxml
c = sxml.PerfmonPort(USERNAME, PASSWORD, HOSTNAME, tls_verify=False)
session = c.PerfmonOpenSession()
counters = [
    {'Name': '\\\\CUCM_PUB\\Number of Replicates Created and State of Replication(ReplicateCount)\\Replicate_State'}
]
result = c.PerfmonAddCounter({'SessionHandle': session, 'ArrayOfCounter': counters})
result = c.PerfmonCollectSessionData({'SessionHandle': session})
print(result)
c.PerfmonCloseSession({'SessionHandle': session})
```

## ControlCenterServicesPort (All Service Control APIs) SOAP Service

```python
import CiscoSXML as sxml
c = sxml.ControlCenterServicesExPort(USERNAME, PASSWORD, HOSTNAME, tls_verify=False)
print(c.list_services())
print(c.getStaticServiceListExtended(''))
```

## LogCollectionPort (All Log Collection APIs) SOAP Service

```python
import CiscoSXML as sxml
c = sxml.LogCollectionPort(USERNAME, PASSWORD, HOSTNAME, tls_verify=False)
print(c.ListNodeServiceLogs())
```

## CDRonDemand (All CDR APIs) SOAP Service

```python
import CiscoSXML as sxml
c = sxml.CDRonDemand(USERNAME, PASSWORD, HOSTNAME, tls_verify=False)
ex = {'in0':'201906051000', 'in1':'201906051200','in2': True}
print(c.get_file_list(ex))
```

## DimeGetFileService (Geting Single File) SOAP Service

```python
import CiscoSXML as sxml
c = sxml.DimeGetFileService(USERNAME, PASSWORD, HOSTNAME, tls_verify=False)
print(c.GetOneFile('/var/log/active/tomcat/logs/catalina.out-20190605').attachments[0].content)
```
