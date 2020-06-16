from marc2jsonl.marc2jsonl import run
from json2marc21.json2marc21 import transpose_to_marc21
import json

def test_marc2json():
    """
    this function tests the MARC21 to JSON functionality
    we read the expected Result into a dict,
    we transform the Marc21 File to a Json dict,
    compare both over json.dumps(sort_keys=True)
    """
    files = ["tests/data_marc1", "tests/data_marc2"]
    for fd in files:
        expected_records = []
        with open("{}.ldj".format(fd)) as inp:
            for line in inp:
                expected_records.append(json.loads(line))
        with open("{}.mrc".format(fd),"rb") as inp:
            for n, record in enumerate(run(inp)):
                assert json.dumps(record,sort_keys=True) == json.dumps(expected_records[n],sort_keys=True)

def test_json2marc():
    """
    this function tests the JSON to MARC21 functionality
    we read the expected MARC21 into a list of the single bytes
    then we transform the JSON File to the MARC21 Bytes which we store
    also as a list of bytes of the single bytes
    now we can compare the both lists, since we can't compare the two BLOBs
    """
    files = ["tests/data_marc1", "tests/data_marc2"]
    for fd in files:
        result = []
        with open("{}.mrc".format(fd), "rb") as inp:
            expected = list(inp.read())
        with open("{}.ldj".format(fd), "rt") as inp:
            for line in inp:
                result+=list(transpose_to_marc21(json.loads(line)))
        assert result == expected
                

