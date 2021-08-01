import sys
from time import sleep
from jina import Document
import csv
import os

import requests
from config import datafile


def check_workspace(dir_name, should_exist=False):
    '''Workspace is a folder which Jina creates everytime it runs. This directory must exist for the command line interface to actually work. So, use this function to ensure that it does. '''
    if should_exist:
        if not os.path.isdir(dir_name):
            print(
                f"The directory {dir_name} does not exist. Please index first via `python app.py -t index`"
            )
            sys.exit(1)

def docs_gen():
    '''Use this function for jina to go through the data and help it index'''
    with open(datafile) as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            with Document() as doc:
                if row[0] != "Hashtags":
                    doc.tags['hash'] = row[0]
                    doc.tags['number'] = row[1]
                    doc.tags['category'] = row[2]
                    doc.text = row[0] + '-' + row[1]

                    yield doc


