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


fname = config['raw']


# COPY THE METADATA CHANNELS.TSV, COORDSYSTEM, ETC ==============================


raw = mne.io.read_raw_fif(fname, preload=True)
raw.interpolate_bads()


# save mne/epochs
raw.save(os.path.join('out_dir','raw.fif'))
