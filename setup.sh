#!/bin/bash

# grab the latest linter
TEMPLATE_LINTER_PATH="https://raw.githubusercontent.com/ndlib/wse-py-template/master/"
TEMPLATE_LINTER_FILE=".flake8"
TEMPLATE_LINTER=${TEMPLATE_LINTER_PATH}${TEMPLATE_LINTER_FILE}

curl ${TEMPLATE_LINTER} -o ${TEMPLATE_LINTER_FILE} -s