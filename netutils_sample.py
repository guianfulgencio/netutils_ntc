from netutils.config.compliance import compliance
from pprint import pprint

features = [
     {
         "name": "aaa",
         "ordered": True,
         "section": [
             "aaa group server tacacs+ ACS"
         ]
     },
     {
         "name": "tacacs",
         "ordered": True,
         "section": [
             "tacacs server"
         ]
     },
     {
        "name": "hostname",
        "ordered": True,
        "section": [
            "hostname"
        ]
        },
        {
        "name": "ntp",
        "ordered": True,
        "section": [
            "ntp"
        ]
        }
 ]


backup = "backup.cfg"

intended = "intended.cfg"

network_os = "cisco_ios"

compliance_report = compliance(features, backup, intended, network_os)

pprint(compliance_report)

for feature_section in compliance_report:
    print(f' {feature_section} config is', 'compliant' if compliance_report[f'{feature_section}']['compliant'] == True else 'non-compliant' )

