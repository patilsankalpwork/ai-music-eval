#!/usr/bin/env python3
"""validate_dataset.py

Basic schema and sanity validation for prompts CSV.
Usage: python3 validate_dataset.py /path/to/prompts_converted.csv
"""
import sys, csv, re

EXPECTED_HEADER = ['prompt_id','genre','description','tempo','keywords','mood','structure','is_vocal']

def load(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows = list(reader)
    return header, rows

def validate_header(header):
    return header == EXPECTED_HEADER

def validate_rows(rows):
    problems = []
    ids = set()
    for i,r in enumerate(rows, start=1):
        pid = r.get('prompt_id','').strip()
        if not re.match(r'^P\d{3}$', pid):
            problems.append((i, pid, 'invalid_id'))
        if pid in ids:
            problems.append((i, pid, 'duplicate_id'))
        ids.add(pid)
        # keywords
        if ';' not in r.get('keywords',''):
            problems.append((i,pid,'keywords_format'))
        # is_vocal
        if r.get('is_vocal','').lower() not in ('yes','no'):
            problems.append((i,pid,'is_vocal_value'))
    return problems

def main():
    if len(sys.argv) < 2:
        print('Usage: validate_dataset.py /path/to/prompts_converted.csv')
        sys.exit(1)
    path = sys.argv[1]
    header, rows = load(path)
    ok_header = validate_header(header)
    if not ok_header:
        print('Header mismatch. Expected:', EXPECTED_HEADER)
        print('Found:', header)
    problems = validate_rows(rows)
    if not problems and ok_header:
        print('Validation passed: {} rows'.format(len(rows)))
    else:
        print('Validation problems (first 20):')
        for p in problems[:20]:
            print(p)

if __name__ == "__main__":
    main()
