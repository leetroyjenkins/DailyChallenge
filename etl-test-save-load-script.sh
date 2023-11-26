#!/bin/bash

#Save timestamp for unique log name
timestamp=$(date +%Y%m%d_%H%M%S)

#Run Pytest and output the results to a json log file in a test_results directory
pytest test_cases.py --no-header --tb=no -q --report-log=pytest-logs/pytestlog_${timestamp}\.json

#Run the python script to load the file to the blob container
python load-tests-to-blob.py