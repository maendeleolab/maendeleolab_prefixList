#!/usr/bin/env python3

import os, json
from build_prefix_list import destroy_prefix_list, erase_prefix_list

#maendeleolab_infra=['us-east-1','us-west-2']
maendeleolab_infra=['us-east-2']

for region in maendeleolab_infra:
	erase_prefix_list(region)

# ------------------------ End ---------------------------
