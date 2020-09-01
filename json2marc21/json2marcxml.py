#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#


import json
import sys
from pymarc import Record, Field, marcxml, MARC8ToUnicode
import xml.etree.ElementTree as ET
from json2marc21.json2marc21 import transpose_to_marc21
from es2json import isint


XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
MARC_XML_NS = "http://www.loc.gov/MARC21/slim"
MARC_XML_SCHEMA = "http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"


def record_to_xml_node(record, quiet=False, namespace=False):
    """
    Function forked from pymarc and put data_field.set("tag") to 2 lines earlier for better readability

    Converts a record object to a chunk of XML.

    If you would like to include the marcxml namespace in the root tag set namespace to
    True.
    """
    # helper for converting non-unicode data to unicode
    # TODO: maybe should set g0 and g1 appropriately using 066 $a and $b?
    marc8 = MARC8ToUnicode(quiet=quiet)

    def translate(data):
        if type(data) == str:
            return data
        else:
            return marc8.translate(data)

    root = ET.Element("record")
    if namespace:
        root.set("xmlns", MARC_XML_NS)
        root.set("xmlns:xsi", XSI_NS)
        root.set("xsi:schemaLocation", MARC_XML_SCHEMA)
    leader = ET.SubElement(root, "leader")
    leader.text = str(record.leader)
    for field in record:
        if field.is_control_field():
            control_field = ET.SubElement(root, "controlfield")
            control_field.set("tag", field.tag)
            control_field.text = translate(field.data)
        else:
            data_field = ET.SubElement(root, "datafield")
            data_field.set("tag", field.tag)
            data_field.set("ind1", field.indicators[0])
            data_field.set("ind2", field.indicators[1])
            for subfield in field:
                data_subfield = ET.SubElement(data_field, "subfield")
                data_subfield.set("code", subfield[0])
                data_subfield.text = translate(subfield[1])
    ET.dump(root)


def main():
    sys.stdout.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<collection xmlns=\"http://www.loc.gov/MARC21/slim\">")
    sys.stdout.flush()
    for line in sys.stdin:
        try:
            record = json.loads(line)
            record = transpose_to_marc21(record, True)
            record_to_xml_node(record, quiet=True, namespace=True)
            sys.stdout.flush()
        except UnicodeDecodeError as e:
            eprint("unicode decode error: {}".format(e))
            eprint(record)
    sys.stdout.write("</collection>\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
