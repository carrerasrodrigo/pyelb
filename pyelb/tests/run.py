# -*- coding: utf-8 -*-
import os
import sys
import unittest

try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pyelb"))

from parser import main


class StdOut(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


class PyElb(unittest.TestCase):
    test_path = os.path.join(os.path.dirname(__file__), 'elb.csv')

    def test_no_args(self):
        self.assertRaises(Exception, main)

    def test_limit_lines(self):
        params = '--col=request_processing_time --file={0} --limit=1' \
            .format(self.test_path)

        with StdOut() as output:
            main(*params.split(' '))
        self.assertEqual(len(output), 1)

    def test_offset(self):
        params = '--col=request_processing_time --file={0} --limit=1 --offset=1' \
            .format(self.test_path)

        with StdOut() as output:
            main(*params.split(' '))
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], '0.000075')

    def test_col(self):
        params = '--col=timestamp --file={0} --limit=1' \
            .format(self.test_path)

        with StdOut() as output:
            main(*params.split(' '))
        self.assertEqual(output[0], '2015-06-13T07:20:24.110235Z')

    def test_order(self):
        params = '--col=request_processing_time --file={0} --limit=1 --order=request_processing_time' \
            .format(self.test_path)

        with StdOut() as output:
            main(*params.split(' '))
        self.assertEqual(output[0], '0.000043')

    def test_order_reverse(self):
        params = '--col=request_processing_time --file={0} --limit=1 --order-reverse=request_processing_time' \
            .format(self.test_path)

        with StdOut() as output:
            main(*params.split(' '))
        self.assertEqual(output[0], '0.000089')


if __name__ == '__main__':
    unittest.main()
