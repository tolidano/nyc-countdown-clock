from defusedxml import ElementTree
import json


def main():
    """
    definition:
    NYCEquipments
    <equipment>
     <station>Whitehall St - South Ferry</station>
     <borough>MN</borough>
     <trainno>R/W</trainno>
     <equipmentno>ES311</equipmentno>
     <equipmenttype>ES</equipmenttype>
     <serving>LOWER MEZZANINE TO UPPER MEZZANINE</serving>
     <ADA>N</ADA>

    xml operations:
    tag, attrib, for child in root, find('tag'), get('attribute'), findall('anytag')
    for recursive_node in root.iter('anytag')
    """
    xml_file = 'allequipments.aspx.xml'
    etree = ElementTree.parse(xml_file)
    equipment_list = []
    for equipment in etree.getroot().iter('equipment'):
        station = equipment.find('station').text
        borough = equipment.find('borough').text
        lines = equipment.find('trainno').text
        identifier = equipment.find('equipmentno').text
        equipment_type = equipment.find('equipmenttype').text
        serving = equipment.find('serving').text
        ada = False
        if equipment.find('ADA').text == 'Y':
            ada = True
        equipment_list.append({
            'station': station,
            'borough': borough,
            'lines': lines,
            'identifier': identifier,
            'type': equipment_type,
            'serving': serving,
            'ada': ada,
            })
    print(json.dumps(equipment_list, indent=1))


if __name__ == '__main__':
    main()
