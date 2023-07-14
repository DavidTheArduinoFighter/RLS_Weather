from Get_Data import Data


def test_temp():
    data = Data()
    if -50 < data.temperature() < 65:
        assert True
    else:
        assert False


def test_wind():
    data = Data()
    if 0 <= data.wind() < 300:
        assert True
    else:
        assert False


def test_humidity():
    data = Data()
    if 0 <= data.humidity() <= 100:
        assert True
    else:
        assert False
