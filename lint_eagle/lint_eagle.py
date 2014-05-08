from lxml import objectify
import argparse
import eagle_lbr
import helper
import sys

#TODO: state contains a list of issues structured like that: $object_name(str), $object_type(component, symbol, package, library, schematic, board, etc.), $issue_type(E1, E2, E3, W1...)



parser = argparse.ArgumentParser(description='Check eagle files for good style. It checks that you use eagle in a sane way instead stressing your luck and hoping that everything will be ok.')
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="count", default=0,help="increase output verbosity")
group.add_argument("-q", "--quiet", action="store_true", default=0,help="quiet")

parser.add_argument('file', action="store", nargs='+', type=argparse.FileType('r'))

args = parser.parse_args(sys.argv[1:])
print (args)



#f = open('test/testfiles/test.lbr', 'r')
#eagle_xml_string = f.read()
#eagle_object = objectify.fromstring(eagle_xml_string)
#lbr_check_name_and_value(eagle_object)
