#!/usr/bin/env python
"""
This aggregates the termvectors for all documents in a multitermvector query
"""

import argparse
import json
from collections import defaultdict

def main():
    """
    Extracts and aggregates the termvectors
    """

    parser = argparse.ArgumentParser(description='Aggregate term information')
    parser.add_argument('files', nargs='+', help='termvector files to load')
    args = parser.parse_args()

    agg = defaultdict(int)
    for filename in args.files:
        with open(filename, 'rb') as handle:
            vectors = json.load(handle)

        for key, freq in (
                term
                for doc in vectors["docs"]
                for term in doc["term_vectors"]["fullText"]["terms"].items()
        ):
            agg[key] += freq["term_freq"]

    print(json.dumps(agg))

if __name__ == '__main__':
    main()
