#!/usr/bin/env python3

import sys
import json

from es2json import eprint, isint
from pymarc import MARCReader
from six.moves import zip_longest as izip_longest


def transpose_to_ldj(record):
    json_record = {
        '_LEADER': record.leader,
        '_FORMAT': "MarcXchange",
        '_TYPE': "Bibliographic"
    }

    for field in record:
        if isint(field.tag):
            if field.is_control_field():
                json_record[field.tag] = [field.data]
            else:
                ind = "".join(field.indicators).replace(" ", "_")
                ind_obj = []
                for k,v in izip_longest(*[iter(field.subfields)] * 2):
                    if "." in ind:
                        ind = ind.replace(".", "_")
                    if "." in k or k.isspace():
                        k="_"
                    ind_obj.append({k: v})
                if not field.tag in json_record:
                    json_record[field.tag] = []
                json_record[field.tag].append({ind: ind_obj})
    return json_record


def run(fd):
    try:
        for record in MARCReader(fd):
            try:
                yield transpose_to_ldj(record)
            except AttributeError as e:
                eprint("attribut error: {}".format(e))
                eprint(record)
                continue
    except UnicodeDecodeError as e:
        eprint("unicode decode error: {}".format(e))
        eprint(record)

def main():
    for record in run(sys.stdin.buffer.read()):
        print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
