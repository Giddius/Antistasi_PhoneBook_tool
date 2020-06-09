import pprint
import sys

import query_from_file


file = sys.argv[1]
output = query_from_file.query_from_file(file)
pprint.pprint(output)
