#!/usr/bin/python3

import os, sys, pprint, itertools
from build_prefix_list import create_prefix_list, get_prefix_list_id
from build_prefix_list import add_prefix_list, remove_prefix_list, get_prefix_list_version
from build_prefix_list import destroy_prefix_list, erase_prefix_list
# path to your home folder /home/username
FPATH = os.environ.get('ENV_FPATH')#ENV_FPATH is a var in your environment variable file
sys.path.append(FPATH+'/maendeleolab_subnet')
import build_subnet

# ----------------------- End ---------------------------
