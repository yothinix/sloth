import time


def test_slow_1():
    time.sleep(1)
    assert True == True

def test_slow_2():
    time.sleep(2)
    assert True == True

def test_slow_3():
    time.sleep(3)
    assert True == True
