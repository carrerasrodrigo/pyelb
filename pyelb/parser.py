#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import csv


COLUMS_ORDER = [
    'timestamp', 'elb', 'client:port', 'backend:port',
    'request_processing_time', 'backend_processing_time',
    'response_processing_time', 'elb_status_code', 'backend_status_code',
    'received_bytes', 'sent_bytes', 'request', 'user_agent',
    'ssl_cipher', 'ssl_protocol', 'total_processing_time']

COLUMS_SPECIAL_ORDER = ['total_processing_time']


def open_file(file_path):
    time_col = get_columns_order('request_processing_time,'
        'backend_processing_time,response_processing_time')
    with open(file_path) as f:
        rows = list(csv.reader(f, delimiter=' '))
    for r in rows:
        val = float(r[time_col[0]]) + float(r[time_col[1]]) + \
            float(r[time_col[2]])
        r += [val]
    return rows


def get_columns_order(columns_text):
    if columns_text == 'all':
        return range(len(COLUMS_ORDER))

    cc = [c.strip() for c in columns_text.split(',')]
    orders = []
    for c in cc:
        if c not in COLUMS_ORDER:
            raise Exception('invalid column type')
        orders.append(COLUMS_ORDER.index(c))
    return orders


def order_data(conf, rows):
    if conf.order is not None:
        index = get_columns_order(conf.order)[0]
        rows.sort(key=lambda x: x[index])
        return rows

    if conf.order_reverse is not None:
        index = get_columns_order(conf.order_reverse)[0]
        rows.sort(key=lambda x: x[index], reverse=True)
        return rows
    return rows


def print_data(conf, column_positions, rows):
    limit = len(rows) if conf.limit is None else conf.limit
    rows = order_data(conf, rows)
    for r in rows[conf.offset:limit+conf.offset]:
        line = u'\t '.join([str(r[d])
            for d in column_positions])
        print(line)


def print_valid_columns():
    print('** File columns **')
    for c in COLUMS_ORDER:
        if c not in COLUMS_SPECIAL_ORDER:
            print(c)

    print('\n** Special columns **')
    for c in COLUMS_SPECIAL_ORDER:
        print(c)
    print('all')



parser = argparse.ArgumentParser(description="pyelb", add_help=True)
parser.add_argument("--file", help="The path of the file that we want to parse", default=None, required=False)
parser.add_argument("--col", help="The name of columns that we want to show", default='all', required=False)
parser.add_argument("--limit", help="limit the number of lines to print", default=None, required=False, type=int)
parser.add_argument("--offset", help="the offset that we want to use to print the data", default=0, required=False, type=int)
parser.add_argument("--order", help="the name of the column that we want to use to order", default=None, required=False)
parser.add_argument("--order-reverse", help="the name of the column that we want to use to order", default=None, required=False, dest='order_reverse')
parser.add_argument("--print-valid-columns", help="shows a list of valid columns to print", default=0, type=int, dest='print_valid_columns')


def main(*args):
    conf = parser.parse_args(args) if len(args) > 0 else parser.parse_args()
    if conf.print_valid_columns == 1:
        print_valid_columns()
        return

    rows = open_file(conf.file)
    column_positions = get_columns_order(conf.col)
    print_data(conf, column_positions, rows)
    return True

if __name__ == '__main__':
    main(*sys.argv[1:])
