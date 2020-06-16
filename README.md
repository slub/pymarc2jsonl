# pymarc2jsonl
MARC21 to MarcXchange formatted ld-JSON and reverse converter based on pymarc

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
pymarc2jsonl and json2marc21 don't use any cmdline arguments, they only use stdout and stdin.

e.g.:
```
pymarc2jsonl < binary_marc21.mrc > line_delmited_json.ldj
```

```
json2marc21 < line_delimited_json.ldj > binary_marc21.mrc
```
