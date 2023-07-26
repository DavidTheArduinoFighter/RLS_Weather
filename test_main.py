from Get_Data import Data

url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
data = Data(url)


def test_temp():
    for value in data.temperature():
        if value[1] is None:
            pass
        elif -50 < float(value[1]) < 65:
            pass
        else:
            print(f'\n\nTemperature value is: {value[1]}')
            assert False
    assert True


def test_rainfall_sum():
    for value in data.rainfall_sum():
        if value[1] is None:
            pass
        elif 0 <= float(value[1]) < 300:
            pass
        else:
            print(f'\n\nRainfall value is: {value[1]}')
            assert False
    assert True


def test_humidity():
    for value in data.humidity():
        if value[1] is None:
            pass
        elif 0 < float(value[1]) < 100:
            pass
        else:
            print(f'\n\nHumidity value is: {value[1]}')
            assert False
    assert True
