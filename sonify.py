#!/usr/bin/env python3
from sonify import sonify
from obspy import UTCDateTime

sonify(
    network='A1',
    station='HRAO',
    channel='HHZ',
    starttime=UTCDateTime(2023, 6, 28, 15, 00),
    endtime=UTCDateTime(2023, 6, 28, 15, 30),
    freqmin=0.5,
    freqmax=49,
    speed_up_factor=40
    fps=1,  # Use fps=60 to fully recreate the JHEPC entry (slow to save!)
    spec_win_dur=8,
    db_lim=(-180, -130),
)
