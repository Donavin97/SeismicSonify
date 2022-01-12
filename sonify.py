#!/usr/bin/env python3
from sonify import sonify
from obspy import UTCDateTime

sonify(
    network='GT',
    station='LBTB',
    channel='SHZ',
    starttime=UTCDateTime(2022, 1, 11, 11, 30),
    endtime=UTCDateTime(2022, 1, 11, 12, 30),
    freqmin=1,
    freqmax=23,
    speed_up_factor=200,
    fps=1,  # Use fps=60 to fully recreate the JHEPC entry (slow to save!)
    spec_win_dur=8,
    db_lim=(-180, -130),
)
