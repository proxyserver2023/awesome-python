#!/usr/bin/env bash


set -eu
# -e => exit if pipeline fails
# -u => treat unset var as errors

failed=""

if which coverage > /dev/null; then
    COVERAGE="`which coverage` run -a"
else
    COVERAGE=''
fi


for f in */[^_]*py; do
    PYTHONPATH=. python $COVERAGE $f || failed+=" $f"
    echo "I: done $f. Exit code $?"
done;

if [ ! -z "$failed" ]; then
    echo "Failed: $failed";
    exit 1
33