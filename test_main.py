from Get_Data import Data

url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'

def test_temp():
    data = Data(url)
    if -50 < data.temperature() < 65:
        assert True
    else:
        assert False


def test_rainfall_sum():
    data = Data(url)
    if 0 <= data.rainfall_sum() < 300:
        assert True
    else:
        assert False


def test_humidity():
    data = Data(url)
    if 0 <= data.humidity() <= 100:
        assert True
    else:
        assert False
