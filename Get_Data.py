import xml.etree.ElementTree as ET
import urllib.request
import requests
from lxml import etree, html
from io import StringIO
from bs4 import BeautifulSoup


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
                sub_output.append(float(value.text))
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
                sub_output.append(float(value.text))
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
                sub_output.append(float(value.text))
            output.append(sub_output)

        return output


class Locations:
    def __init__(self, url):
        response = requests.get(url)
        self.data = html.fromstring(response.content)

    def locations(self):
        locations_all = self.data.xpath('//table[@class="tableLocations"]/tr/td[1]/a/text()')
        location_xml_list = self.data.xpath('//table[@class="tableLocations"]/tr/td[13]/a/@href')  # /@href

        locations_valid = []

        # if xml doesn't exist, skip location
        for i in range(1, len(locations_all)):
            locations = self.data.xpath(f'//table[@class="tableLocations"]/tr[{i}]/td[1]/a/text()')
            loc_line = self.data.xpath(f'//table[@class="tableLocations"]/tr[{i}]/td[@colspan="11"]/text()')
            if len(loc_line) > 0:
                locations_valid.extend(locations[1:3])
            else:
                locations_valid.extend(locations)

        output = [locations_valid, location_xml_list]

        return output


if __name__ == '__main__':
    # url_test = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
    # data_test = Data(url_test)
    # data = data_test.temperature()
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]))
    # data = data_test.rainfall_sum()
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]))
    # data = data_test.humidity()
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]))

    url_test = 'http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1'
    web_data = Locations(url_test)
    data = web_data.locations()
    print(data)

