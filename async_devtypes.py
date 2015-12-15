import netsnmp
from netsnmp._dev import cisco

# temporary
SNMP_DEVTYPES = {
        'archt01': cisco.SNMPCiscoDevice([
            ('sysHostname', '.1.3.6.1.2.1.1.5.0'),
            ('HexMacAddr', '.1.3.6.1.2.1.55.1.5.1.8.2'),
        ]), #hexconvert=['.1.3.6.1.2.1.55.1.5.1.8.2']), Define hexconvert here or in SNMPCiscoDevice class
        'archt02': cisco.SNMPCiscoDevice(),
        'archt03': cisco.SNMPCiscoDevice([
            ('1min', '.1.3.6.1.4.1.2021.10.1.3.1'),
            #('5min', '.1.3.6.1.4.1.2021.10.1.3.2'),
            #('15min', '.1.3.6.1.4.1.2021.10.1.3.3'),
        ]),
        'archt04': cisco.SNMPCiscoDevice([
            #('1min', '.1.3.6.1.4.1.2021.10.1.3.1'),
            ('5min', '.1.3.6.1.4.1.2021.10.1.3.2'),
            ('15min', '.1.3.6.1.4.1.2021.10.1.3.3'),
        ]),
        'archt05': netsnmp._dev.SNMPDevice([
            ('sysDescr', '.1.3.6.1.2.1.1.1.0'),
            #('1min', '.1.3.6.1.4.1.2021.10.1.3.1'),
            #('5min', '.1.3.6.1.4.1.2021.10.1.3.2'),
            ('15min', '.1.3.6.1.4.1.2021.10.1.3.3'),
        ]),
        'Belair': netsnmp._dev.SNMPDevice([
            ('model', '.1.3.6.1.2.1.1.1.0'),
            ('serial_number', '.1.3.6.1.4.1.15768.3.1.1.11.2.0'),
            ('tunnel_peer1', '.1.3.6.1.4.1.15768.5.1.1.2.1.5.1.1'),
            ('tunnel_peer2', '.1.3.6.1.4.1.15768.5.1.1.2.1.9.1.1'),
            ('swbank_active', '.1.3.6.1.4.1.15768.3.1.1.3.1.0'),
            ('swbank_next', '.1.3.6.1.4.1.15768.3.1.1.3.2.0'),
            ('software_a', '.1.3.6.1.4.1.15768.3.1.1.3.5.1.2.1'),
            ('software_b', '.1.3.6.1.4.1.15768.3.1.1.3.5.1.2.2'),
            ('tunnel_status', '.1.3.6.1.4.1.15768.5.1.1.3.1.1.1.1'),
            ('vpn_label', '.1.3.6.1.4.1.15768.5.1.1.2.1.2.1.1'),
            ('tunnel1_active', '.1.3.6.1.4.1.15768.5.1.1.3.1.3.1.1'),
            ('tunnel2_active', '.1.3.6.1.4.1.15768.5.1.1.3.1.4.1.1'),
            ('radius_server1', '.1.3.6.1.2.1.67.1.2.1.1.3.1.2.1'),
            ('radius_server2', '.1.3.6.1.2.1.67.1.2.1.1.3.1.2.2'),
            #('cm.software', '.1.3.6.1.4.1.15768.6.4.1.1.1.5.1'),
        ]),
        '__default__': netsnmp._dev.SNMPDevice([
            ('model', '.1.3.6.1.2.1.1.1.0'),
            ('hostn', '.1.3.6.1.2.1.1.5.0'),
        ]),
}

