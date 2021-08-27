#!/usr/bin/env python3

import os
import sys
from pathlib import Path

this_file = sys.argv[0]
this_dir = Path(this_file).parent # .resolve() use .resolve() to get full paths


for dirpath, dirnames, filenames in os.walk(this_dir):
    print(f"dirpath={dirpath}")
    print(f"|- dirnames={dirnames}")
    print(f"|--* filenames={filenames}")
# dirpath=os_lib
# |- dirnames=['walk_example']
# |--* filenames=['walking_basics.py']
# dirpath=os_lib/walk_example
# |- dirnames=['painkiller', 'antibiotics']
# |--* filenames=['readme.md']
# dirpath=os_lib/walk_example/painkiller
# |- dirnames=['nsaid', 'other', 'ion-channel-modulators']
# |--* filenames=['analgesics-source-link.txt']
# dirpath=os_lib/walk_example/painkiller/nsaid
# |- dirnames=[]
# |--* filenames=['diclofenac.txt', 'ibuprofen.txt']
# dirpath=os_lib/walk_example/painkiller/other
# |- dirnames=[]
# |--* filenames=['aspirin.txt']
# dirpath=os_lib/walk_example/painkiller/ion-channel-modulators
# |- dirnames=['sodium-blockers']
# |--* filenames=[]
# dirpath=os_lib/walk_example/painkiller/ion-channel-modulators/sodium-blockers
# |- dirnames=[]
# |--* filenames=['carbamazepine.txt']
# dirpath=os_lib/walk_example/antibiotics
# |- dirnames=['cell-wall-envelope-targeted-drugs', 'protein-synthesis-inhibitors']
# |--* filenames=['source.txt']
# dirpath=os_lib/walk_example/antibiotics/cell-wall-envelope-targeted-drugs
# |- dirnames=['penicillins', 'penems']
# |--* filenames=[]
# dirpath=os_lib/walk_example/antibiotics/cell-wall-envelope-targeted-drugs/penicillins
# |- dirnames=[]
# |--* filenames=['amoxicillin.txt']
# dirpath=os_lib/walk_example/antibiotics/cell-wall-envelope-targeted-drugs/penems
# |- dirnames=[]
# |--* filenames=[]
# dirpath=os_lib/walk_example/antibiotics/protein-synthesis-inhibitors
# |- dirnames=[]
# |--* filenames=['streptomycin.txt', 'doxycycline.txt']

