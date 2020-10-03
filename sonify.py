from sonify import sonify
from obspy import UTCDateTime

sonify(
    network='GT',
    station='LBTB',
    channel='BHZ',
    starttime=UTCDateTime(2020, 7, 7, 10, 00),
    endtime=UTCDateTime(2020, 7, 7, 12, 00),
    freqmin=1,
    freqmax=23,
    speed_up_factor=200,
    fps=1,  # Use fps=60 to fully recreate the JHEPC entry (slow to save!)
    spec_win_dur=8,
    db_lim=(-180, -130),
)
