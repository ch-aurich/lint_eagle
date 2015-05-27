from lxml import objectify
import argparse
import eagle_lbr
import eagle_brd
#import helper
import sys

import lint_framework

#TODO: state contains a list of issues structured like that: $object_name(str), $object_type(component, symbol, package, library, schematic, board, etc.), $issue_type(E1, E2, E3, W1...)



parser = argparse.ArgumentParser(description='Check eagle files for good style. It checks that you use eagle in a sane way instead stressing your luck and hoping that everything will be ok.')
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="count", default=0,help="increase output verbosity")
group.add_argument("-q", "--quiet", action="store_true", default=0,help="quiet")

parser.add_argument('file', action="store", nargs='+', type=argparse.FileType('rb'))

args = parser.parse_args(sys.argv[1:])
#print (args)


for file_handle in args.file:
  issues = []
  
  eagle_xml_string = file_handle.read()
  eagle_object = objectify.fromstring(eagle_xml_string)

  issues += eagle_lbr.lbr_check_name_and_value_package(eagle_object, args)
  issues += eagle_brd.brd_check_testpad_on_all_nets(eagle_object, args)
  print ("testing file: \"" + str(file_handle.name) + "\"\n")
  for issue in issues:
    print("\t" + str(issue))

if issues == []:
  sys.exit(0)
else:
  sys.exit(1)
