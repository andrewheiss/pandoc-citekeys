#!/usr/bin/env python3

# Extract all citation keys from a BibTeX file and save them to a list that
# can then be used in TextExpander, following these steps:
#
# 1. In TextExpander, select "Add Group from URL" and type the local URL for 
# the list of keys: file://localhost/Users/path/to/keys.txt. 
# This file will update once a day, but can be manually updated too.
#
# 2. Set a hotkey for "Suggest Matching Abbreviations" and/or "Search Snippets"
# and use it to insert a pandoc-markdown-style citation key using TextExpander's 
# fuzzy searching.
#
# Inspired and adapted from David Sanson's Ruby script 
# (https://gist.github.com/dsanson/580866) and original post at
# https://groups.google.com/d/msg/pandoc-discuss/ddQb5xVjNRE/J3Nnv38rHysJ
#
# Usage: bib_keys.py [-h] filename [output]
#

# Load libraries
import argparse
import re
import sys

# Get command line information
parser = argparse.ArgumentParser(description='Convert a BibTeX file to a list of keys for TextExpander.')
parser.add_argument('filename', type=argparse.FileType('r'), 
                    help='the path to a BibTeX file')
parser.add_argument('output', type=argparse.FileType('w'), 
                    nargs='?', default=sys.stdout, 
                    help='the name of the output file (defaults to stdout)')
args = parser.parse_args()

# Save arguments
bib = args.filename
output = args.output

# Read bibliography
bibfile = bib.read()

# Get a sorted list of all citekeys
bibkeys = sorted(re.findall("@.*?{(.*?),", bibfile))

# Write citekeys to file in TextExpander format (",@citekey")
with output as f:
  for entry in bibkeys:
    f.write(",@{0}".format(entry) + '\n')
