import asyncio
from pysnmp.hlapi.asyncio import *
from pysnmp.smi.rfc1902 import ObjectIdentity, ObjectType

from datetime import datetime

loop = asyncio.get_event_loop()
snmpEngine = SnmpEngine()


async def run_get():
    errorIndication, errorStatus, errorIndex, varBinds = await getCmd(
        snmpEngine,
        CommunityData('community_string'),
        UdpTransportTarget(('1.2.3.4', 161), timeout=2, retries=0),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')),
    )
    for varBind in varBinds:
        print([str(varBind[0]), varBind[1]])

print("start " + datetime.now().strftime("%H:%M:%S"))
loop.run_until_complete(run_get())
snmpEngine.transportDispatcher.closeDispatcher()
print("end " + datetime.now().strftime("%H:%M:%S"))
