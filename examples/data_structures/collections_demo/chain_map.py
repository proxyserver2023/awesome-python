"""
>>> import builtins
>>> import collections

>>> pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
"""

import collections
import os, argparse

defaults = {'color': 'red',
            'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')

namespace = parser.parse_args()
command_line_args = {
    k:v for k, v in vars(namespace).items() if v
}
combined = collections.ChainMap(
    command_line_args,
    os.environ,
    defaults
)

import pprint
pprint.pprint(combined)

"""
in cli -> python chain_map.py -u username -c colorname
"""