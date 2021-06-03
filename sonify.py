from sonify import sonify
from obspy import UTCDateTime

sonify(
    network='GT',
    station='LBTB',
    channel='SHZ',
    starttime=UTCDateTime(2021, 6, 3, 2, 30),
    endtime=UTCDateTime(2021, 6, 3, 4, 00),
    freqmin=1,
    freqmax=23,
    speed_up_factor=100,
    fps=1,  # Use fps=60 to fully recreate the JHEPC entry (slow to save!)
    spec_win_dur=8,
    db_lim=(-180, -130),
)
