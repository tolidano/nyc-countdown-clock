import argparse
from defusedxml import ElementTree
import os
import sys


def main(xml_file):
    """
    definition:
    Siri
     ServiceDelivery
      SituationExchangeDelivery
       ResponseTimestamp
       Status
       Situations (Array)
        PtSituationElement
         CreationTime
         SituationNumber
         PublicationWindow
          StartTime
          EndTime
         Summary
         Description
         LongDescription
         Planned
         ReasonName
         Source
          SourceType
         Affects
          VehicleJourneys (Array)
           AffectedVehicleJourney
            LineRef
            DirectionRef
         Consequences (Array)
          Consequence
           Condition
           Severity

    xml operations:
    tag, attrib, for child in root, find('tag'), get('attribute'), findall('anytag')
    for recursive_node in root.iter('anytag')
    """
    print('XML file selected: ' + xml_file)
    etree = ElementTree.iterparse(xml_file)
    for _, el in etree:
        el.tag = el.tag.split('}', 1)[1]
    situations = []
    for situation in etree.root.iter('PtSituationElement'):
        creation_time = situation.find('CreationTime').text
        situation_number = situation.find('SituationNumber').text
        start_time = situation.find('PublicationWindow').find('StartTime').text
        end_time = None
        if situation.find('PublicationWindow').find('EndTime'):
            end_time = situation.find('PublicationWindow').find('EndTime').text
        summary = situation.find('Summary').text
        description = situation.find('Description').text
        long_description = situation.find('LongDescription').text
        planned = situation.find('Planned').text
        reason = situation.find('ReasonName').text
        source_type = situation.find('Source').find('SourceType').text
        affects = []
        for journey in situation.find('Affects').find('VehicleJourneys'):
            affects.append({'LineRef': journey.find('LineRef').text, 'DirectionRef': journey.find('DirectionRef').text})
        consequences = []
        for consequence in situation.find('Consequences'):
            consequences.append({'Condition': consequence.find('Condition').text, 'Severity': consequence.find('Severity').text})
        situations.append({
            'CreationTime': creation_time,
            'SituationNumber': situation_number,
            'StartTime': start_time,
            'EndTime': end_time,
            'Summary': summary,
            'Description': description,
            'LongDescription': long_description,
            'Planned': planned,
            'Reason': reason,
            'SourceType': source_type,
            'Journeys': affects,
            'Consequences': consequences,
            });
    print(situations)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('xml_file', help='File to parse')
    ARGS = PARSER.parse_args()
    if not ARGS.xml_file or not os.path.exists(ARGS.xml_file):
        print('Must supply a valid XML file.')
        sys.exit()
    main(ARGS.xml_file)
