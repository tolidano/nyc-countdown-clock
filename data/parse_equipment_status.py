from defusedxml import ElementTree
import json
import os
import sys


def main():
    """
    definition:
    <outage>
     <station>179 St - Jamaica</station>
     <borough>QNS</borough>
     <trainno>F</trainno>
     <equipment>EL431</equipment>
     <equipmenttype>EL</equipmenttype>
     <serving>STREET TO MEZZANINE</serving>
     <ADA>Y</ADA>
     <outagedate>11/22/2017 12:30:00 AM</outagedate>
     <estimatedreturntoservice>11/22/2017  4:30:00 AM</estimatedreturntoservice>
     <reason>INSPECTION</reason>
     <isupcomingoutage>Y</isupcomingoutage>
     <ismaintenanceoutage>N</ismaintenanceoutage>
    </outage>

    xml operations:
    tag, attrib, for child in root, find('tag'), get('attribute'), findall('anytag')
    for recursive_node in root.iter('anytag')
    """
    xml_file = 'nyct_ene.xml'
    etree = ElementTree.parse(xml_file)
    outages = []
    for outage in etree.getroot().iter('outage'):
        station = outage.find('station').text
        borough = outage.find('borough').text
        line = outage.find('trainno').text
        equipment = outage.find('equipment').text
        equipment_type = outage.find('equipmenttype').text
        serving = outage.find('serving').text
        ada = False
        if outage.find('ADA').text == 'Y':
            ada = True
        reason = outage.find('reason').text
        upcoming = False
        if outage.find('isupcomingoutage').text == 'Y':
            upcoming = True
        maintenance = False
        if outage.find('ismaintenanceoutage').text == 'Y':
            maintenance = True
        outage_date = outage.find('outagedate').text
        return_date = None
        if outage.find('estimatedreturntoservice').text:
            return_date = outage.find('estimatedreturntoservice').text
        outages.append({
            'station': station,
            'borough': borough,
            'line': line,
            'equipment': equipment,
            'type': equipment_type,
            'serving': serving,
            'ada': ada,
            'reason': reason,
            'upcoming': upcoming,
            'maintenance': maintenance,
            'outage_date': outage_date,
            'return_date': return_date,
            });
    print(json.dumps(outages, indent=1))


if __name__ == '__main__':
    main()
