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
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
                    0: (start_time, start_time.shift(hours=1)),
                    50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3.5)),
                    150: (start_time.shift(), start_time.shift(hours=1)),
                    200: (start_time.shift(), start_time.shift(hours=1)),
                    }

    for km, time_tuple in checkpoint.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

