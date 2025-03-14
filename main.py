# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Contributor: Kami Salibayeva
# Indiana University

# set up environment
import os
import json
import mne

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# if there's a "tags" field in config.json, collect it in a list
if 'tags' in config:
    in_tags = config['tags']

fname = config['raw']


# COPY THE METADATA CHANNELS.TSV, COORDSYSTEM, ETC ==============================


raw = mne.io.read_raw_fif(fname, preload=True)

bads = raw.info['bads']

raw.interpolate_bads()


# save mne/epochs
raw.save(os.path.join('out_dir','raw.fif'))

dict_json_product = {'brainlife': []}


# add a message to the product.json
info = 'Interpolated bad channels: ' + str(bads)
info = str(info)

dict_json_product['brainlife'].append({'type': 'info', 'msg': info})

# if in_tags is not empty, add it to the product.json
if in_tags:
    dict_json_product['tags'] = in_tags
    

with open('product.json', 'w') as outfile:
    json.dump(dict_json_product, outfile)
    
