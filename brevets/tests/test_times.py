"""
Nose tests for acp_times.py

We cannot test for randomness here (no effective oracle),
but we can test that the elements in the returned string
are correct.
"""
from acp_times import *
import arrow
import nose    # Testing framework

FORMAT = 'YYYY-MM-DDTHH:mm'

start = arrow.get("2021-01-01 00:00")

def test_open_200km():
	got = open_time(70, 200, start).format(FORMAT)
	assert got == '2021-01-01T02:04', '%s does not match' % got

# def test_close_200km():
	# got = close_time(70, 200, start).format(FORMAT)
	# assert got == '2021-01-01T04:40', '%s does not match' % got

def test_open_20percent():
	got = open_time(240, 200, start).format(FORMAT)
	assert got == '2021-01-01T05:53', '%s does not match' % got

def test_close_20percent():
	got = close_time(240, 200, start).format(FORMAT)
	assert got == '2021-01-01T13:30', '%s does not match' % got

def test_close_60km():
	got = close_time(60, 200, start).format(FORMAT)
	assert got == '2021-01-01T04:00', '%s does not match' % got

# def test_open_890km():
	# got = open_time(890, 1000, start).format(FORMAT)
	# assert got == '2021-01-02T05:09', '%s does not match' % got

def test_close_890km():
	got = close_time(890, 1000, start).format(FORMAT)
	assert got == '2021-01-03T17:23', '%s does not match' % got

if __name__ == "__main__":
    nose.main()