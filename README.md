<img alt="EFRE-Lod logo" src="https://raw.githubusercontent.com/slub/data.slub-dresden.de/master/assets/images/EFRE_EU_quer_2015_rgb_engl.svg" width="300" >

# pymarc2jsonl
MARC21 to MarcXchange formatted ld-JSON and reverse converter based on pymarc. Also converts to MARC-XML.

## requirements
  - [es2json](https://github.com/slub/es2json)
  - [six](https://github.com/benjaminp/six)
  - [pymarc](https://gitlab.com/pymarc/pymarc)

## Installation
Clone this Repository, cd into it and run:
```
python3 -m pip install --user .
```
## usage
pymarc2jsonl, json2marc21 and json2marcxml don't use any cmdline arguments, they only use stdout and stdin.

e.g.:
```
pymarc2jsonl < binary_marc21.mrc > line_delmited_json.ldj
```

```
json2marc21 < line_delimited_json.ldj > binary_marc21.mrc
```

```
json2marcxml < line_delimited_json.ldj > xml_marc.xml
```

## Tests
this package comes with tests, run via:

```
python3 -m pytest tests/
```
