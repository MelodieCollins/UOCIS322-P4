"""
Nose tests for acp_times.py

We cannot test for randomness here (no effective oracle),
but we can test that the elements in the returned string
are correct.
"""
from acp_times import *
import arrow
import nose    # Testing framework

start = arrow.get("2021-01-01 00:00")

def test_open_200km():
	assert open_time(70, 200, start).format('YYYY-MM-DDTH:mm') == '2021-01-01T02:04'

def test_close_200km():
	assert close_time(70, 200, start).format('YYYY-MM-DDTH:mm') == '2021-01-01T04:40'

def test_open_20percent():
	assert open_time(240, 200, start).format('YYYY-MM-DDTH:mm') == '2021-01-01T05:53'

def test_close_20percent():
	assert close_time(240, 200, start).format('YYYY-MM-DDTH:mm') == '2021-01-01T13:30'
#?
def test_close_60km():
	assert close_time(60, 200, start).format('YYYY-MM-DDTH:mm') == '2021-01-01T4:00'

def test_open_890km():
	assert close_time(890, 1000, start).format('YYYY-MM-DDTH:mm') == '2021-01-02T05:09'

def test_close_890km():
	assert close_time(890, 1000, start).format('YYYY-MM-DDTH:mm') == '2021-01-03T17:23'

print(nose.run())