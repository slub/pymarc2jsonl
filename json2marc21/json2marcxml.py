#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#


import json
import sys
from pymarc import Record, Field, marcxml
from json2marc21 import transpose_to_marc21
from es2json import isint


def main():
    sys.stdout.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    sys.stdout.flush()
    for line in sys.stdin:
        try:
            record = json.loads(line)
            record = transpose_to_marc21(record)
            sys.stdout.buffer.write(marcxml.record_to_xml(record,quiet=False))
            sys.stdout.flush()
        except UnicodeDecodeError as e:
            eprint("unicode decode error: {}".format(e))
            eprint(record)


if __name__ == "__main__":
    main()
