"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_brevet1():
    start_time = arrow.get("2023-02-18 08:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
                    0: (start_time, start_time.shift(hours=1)),
                    50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
                    150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
                    200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=30)),
                    }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet2():
    start_time = arrow.get("2023-04-04 13:00", "YYYY-MM-DD HH:mm")
    dist = 300
    checkpoints = {
                    0: (start_time, start_time.shift(hours=1)),
                    60: (start_time.shift(hours=1, minutes=46), start_time.shift(hours=4)),
                    120: (start_time.shift(hours=3, minutes=32), start_time.shift(hours=8)),
                    180: (start_time.shift(hours=5, minutes=18), start_time.shift(hours=12)),
                    240: (start_time.shift(hours=7, minutes=8), start_time.shift(hours=16)),
                    300: (start_time.shift(hours=9), start_time.shift(hours=20)),
                    }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close