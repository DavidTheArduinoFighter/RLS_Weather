import xml.etree.ElementTree as ET
import urllib.request


class Data:
    def __init__(self, url):
        response = urllib.request.urlopen(url).read()
        self.tree = ET.fromstring(response)

    def temperature(self):
        output = []
        for meta in self.tree.findall('metData'):
            sub_output = []
            date = meta.find('valid')
            value = meta.find('tavg')
            if date is None:
                sub_output.append(None)
            else:
                sub_output.append(date.text)
            if value is None:
                sub_output.append(None)
            else:
                sub_output.append(value.text)
            output.append(sub_output)

        return output

    def rainfall_sum(self):
        output = []
        for meta in self.tree.findall('metData'):
            sub_output = []
            date = meta.find('valid')
            value = meta.find('rr')
            if date is None:
                sub_output.append(None)
            else:
                sub_output.append(date.text)
            if value is None:
                sub_output.append(None)
            else:
                sub_output.append(value.text)
            output.append(sub_output)

        return output

    def humidity(self):
        output = []
        for meta in self.tree.findall('metData'):
            sub_output = []
            date = meta.find('valid')
            value = meta.find('rhavg')
            if date is None:
                sub_output.append(None)
            else:
                sub_output.append(date.text)
            if value is None:
                sub_output.append(None)
            else:
                sub_output.append(value.text)
            output.append(sub_output)

        return output


if __name__ == '__main__':
    url_test = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
    data_test = Data(url_test)
    data = data_test.temperature()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]))
    data = data_test.rainfall_sum()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]))
    data = data_test.humidity()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]))
