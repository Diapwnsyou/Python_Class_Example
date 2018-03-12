#!/usr/bin/env python

import argparse
from net_tools import *

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description=('''A simple demo script using a
                                                  network tools class.'''))
   parser.add_argument('-n', '--name', dest='target', required=True,
                       help='Required hostname for target device')

   args = parser.parse_args()

   device = nettools(args.target)

   print device.tracer(full=False)
