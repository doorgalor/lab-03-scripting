#!/bin/bash
set -euo pipefail

curl -sSL -o lab3-bundle.tar.gz https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

tar -xzf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

ROWS=$(tail -n +2 cleaned.csv | wc -l | tr -d ' ')
echo "Data rows remaining: $ROWS"

tar -czf converted-archive.tar.gz cleaned.csv
