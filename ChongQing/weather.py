import requests

import re
import pandas as pd


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
        '''获取网页html'''
        response = requests.get(self.url)

        #设置编码格式为gbk
        response.encoding = 'gbk'
        html = response.text
        response.close()

        return html

    def parse_html(self,bs,html):
        '''解析网页html'''

        #查找城市名称
        self.name = '重庆'

        '''查找日期、最高温度、最低温度'''
        table = bs.find(name='table',attrs={'width':'100%'})

        # 查找日期
        for a in table.find_all(name='a'):
            date = str(a.string).strip()
            self.dates.append(date)

        #利用正则表达式查找最高/最低温度
        pattern = re.compile('<td>.*?href.*?</a>.*?<td>.*?<td>(.*?)</td>',re.S)
        items = re.findall(pattern,html)
        for item in items:
            # 查找最高温度
            if (item.strip()[0:1] and item.strip()[1:2]) in [str(x) for x in range(0,10)]:
                max = item.strip()[0:2]
            else:
                max = item.strip()[0:1]
            self.Maximum_temperature.append(max)
            # 查找最低温度
            min = item.strip()[-3:-1]
            self.Minimum_temperature.append(min)


    def write_to_file(self,dates,maxs,mins,i):
        '''将数据写入csv文件'''
        #利用pandas，向csv逐列添加数据
        dataframe = pd.DataFrame({'日期':dates,'最高温度':maxs,'最低温度':mins})
        #设置后面添加的数据不添加列名
        if i == 1:
            dataframe.to_csv(r'cq_weather_data.csv',sep=',',encoding='gbk',mode='a',index=False)
        else:
            dataframe.to_csv(r'cq_weather_data.csv',sep=',',encoding='gbk',mode='a',index=False,header=False)


