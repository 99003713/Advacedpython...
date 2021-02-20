import pytest
from mytrip import *


@pytest.fixture
def my_trip():
    OBJ2 = FlightTrip("chennai", "delhi", 1000, "indigo", 500)
    return OBJ2


def test_fare_one(my_trip):
    assert my_trip.compute_fare() == 20000

def test_time_one(my_trip):
    assert my_trip.compute_travel_time() == 2.0
