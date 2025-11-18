#!/usr/bin/env python3
"""analyze_results.py

Aggregate rater CSV files and compute basic statistics.
Usage: python3 analyze_results.py /path/to/rater_sheet.csv
"""
import sys, csv, statistics
def main(path):
    scores = []
    with open(path,newline='',encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                scores.append(float(row.get('composite_score',0)))
            except:
                pass
    if not scores:
        print('No composite_score values found.')
        return
    print('N=', len(scores))
    print('Mean=', statistics.mean(scores))
    print('Std=', statistics.pstdev(scores))
if __name__=='__main__':
    if len(sys.argv)<2:
        print('Usage: analyze_results.py /path/to/rater_sheet.csv')
    else:
        main(sys.argv[1])
