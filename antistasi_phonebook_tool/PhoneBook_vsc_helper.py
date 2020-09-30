import pprint
import sys

import query_from_file
import query_from_fnc

file = sys.argv[1]
if '.sqf' in file:
    output = query_from_file.query_from_file(file)
elif '_fnc_' in file:
    output = query_from_fnc.query_from_fnc(file)
pprint.pprint(output)
