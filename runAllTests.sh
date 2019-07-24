#!/usr/bin/env bash

testFolder=$(pwd)/tests
for testFile in $testFolder/*; do
	echo "TESTING CASE: " $testFile
	python3 tp.py < $testFile
done
