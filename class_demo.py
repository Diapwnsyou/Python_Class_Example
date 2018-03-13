#!/usr/bin/env python

import argparse
import sys
from net_tools import *

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description=('''A simple demo script using a
                                                  network tools class.'''))
   parser.add_argument('-n', '--name', dest='target', required=True,
                       help='Required hostname for target device')
   parser.add_argument('-p', '--ping', dest='ping', action='store_true',
                       help='Pings target')
   parser.add_argument('-t', '--trace', dest='trace', action='store_true',
                       help='Traces to target via traceroute')

   args = parser.parse_args()

   device = nettools(args.target)

   if args.ping:
       if device.pinger():
           print '{}: Responded to ping test'.format(args.target)
       else:
           print '{}: Failed ping check'.format(args.target)

   if args.trace:
       traceoutput = device.tracer()
       if not traceoutput:
           print 'Trace longer than 22 hops most likely failed'
       else:
           print 'Trace hops output:'
           for ips in traceoutput:
               print '  {}'.format(ips)
