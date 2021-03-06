#!/usr/bin/env python

import argparse
import io
import sys

from lib.pg_tools import run_sql_test
from lib.tools import show_status, show_result

def perform_tests(version):
    success = True

    show_status('Testing PostgreSQL {version}...'.format(version=version))

    show_status('Testing read...')
    if not show_result(version, 'read', run_sql_test('read.sql')):
        success = False

    show_status('Testing query...')
    if not show_result(version, 'query', run_sql_test('query.sql')):
        success = False

    return success

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set up testing environment.')
    parser.add_argument('version', help='PostgreSQL version')
    args = parser.parse_args()

    version = args.version
    success = perform_tests(version)
    sys.exit(0 if success else 1)
