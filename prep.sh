#!/bin/sh
# https://spacy.io/docs#getting-started
virtualenv .env
source .env/bin/activate
pip install spacy
python -m spacy.en.download
