#!/usr/bin/python
import sys

def main(argv):
   a=180000
   b=1.05
   c=30
   n=0
   for i in range(0,c):
       n=n*b+a
       print "Year",i,": ",n

# Main entry
if __name__ == '__main__':
    main(sys.argv)
