

import requests
import csv


class Weather():
    '''创建一个关于爬取天气的类'''
    def __init__(self,url):
        '''初始化属性'''
        self.url = url
        self.name = None
        self.dates = []
        self.Maximum_temperature = []
        self.Minimum_temperature = []

    def get_html(self):
        response = requests.get(self.url)

        #设置编码格式为utf-8
        response.encoding = 'utf-8'
        html = response.text

        return html

    def parse_html(self,bs):
        #查找城市名称
        self.name = bs.title.string

        #查找日期、最高温度

        for li in bs.find_all(name='ul',attrs={'class':'t clearfix'}):
            # 查找日期
            for h1 in li.find_all(name='h1'):
                date = str(h1.string)
                self.dates.append(date)
            self.dates.insert(0,'日期')

            #查找最高温度
            for p_tag in li.find_all(name='p',attrs={'class':'tem'}):
                for tem in p_tag.find_all(name='span'):
                    maxtem = int(str(tem.string)[0:2])
                    self.Maximum_temperature.append(maxtem)
            self.Maximum_temperature.insert(0, 0)
            self.Maximum_temperature.insert(0,'最高温度')

            #查找最低温度
            for p_tag in li.find_all(name='p',attrs={'class':'tem'}):
                for tem in p_tag.find_all(name='i'):
                    mintem = int(str(tem.string)[0:2])
                    self.Minimum_temperature.append(mintem)
            self.Minimum_temperature.insert(0, '最低温度')

    def write_to_file(self,title,dates,maxs,mins):
        with open('weather_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(title)
            writer.writerow(dates)
            writer.writerow(maxs)
            writer.writerow(mins)
            print('写入文件完毕')