#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#


import json
import sys
import collections
from pymarc import Record, Field
from es2json import isint


def transpose_to_marc21(record, fix_xml):
    Mrecord = Record(force_utf8=True)
    Mrecord.leader = record["_LEADER"]
    for field in collections.OrderedDict(sorted(record.items())):
        if isint(field):
            if int(field) < 10:
                if isinstance(record[field], list):
                    for elem in record[field]:
                        Mrecord.add_field(Field(tag=field, data=elem))
                elif isinstance(record[field], str):
                    Mrecord.add_field(Field(tag=field, data=record[field]))
            else:
                for subfield in record[field]:
                    for ind, values in subfield.items():
                        indicators = []
                        subfields = []
                        for elem in values:
                            for k, v in elem.items():
                                if isinstance(v, str):
                                    subfields.append(k)
                                    subfields.append(v)
                                elif isinstance(v, list):
                                    for subfield_elem in v:
                                        subfields.append(k)
                                        subfields.append(subfield_elem)
                        for elem in ind:
                            if fix_xml and elem == '_':
                                indicators.append(' ')
                            else:
                                indicators.append(elem)
                        Mrecord.add_field(Field(tag=str(field),
                                                indicators=indicators,
                                                subfields=subfields))
    return Mrecord


def main():
    for line in sys.stdin:
        try:
            record = json.loads(line)
            record = transpose_to_marc21(record, False)
            sys.stdout.buffer.write(record.as_marc())
            sys.stdout.flush()
        except UnicodeDecodeError as e:
            eprint("unicode decode error: {}".format(e))
            eprint(record)


if __name__ == "__main__":
    main()
