#!/usr/bin/env python
"""
This populates elasticsearch with the pickled json data provided
"""

import argparse
import pickle
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def main(): # pylint: disable=missing-docstring
    parser = argparse.ArgumentParser(description='Populate elasticsearch with pickled data')
    parser.add_argument('files', nargs='+', help='Python pickle files to load')
    parser.add_argument(
        '--es-host', default='127.0.0.1:9200', help='Elasticsearch hostname and port'
    )
    args = parser.parse_args()

    client = Elasticsearch([args.es_host], sniff_on_start=True)

    for filename in args.files:
        load(client, filename)

def load(client, filename):
    """ This loads the data """
    with open(filename, "rb") as handle:
        data = pickle.load(handle)

    bulk(client, ({**entry, '_index': 'documents', '_type': 'document'} for entry in data))

if __name__ == '__main__':
    main()
