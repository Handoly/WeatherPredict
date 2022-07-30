from bs4 import BeautifulSoup
from weather import Weather


if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101040300.shtml'
    w = Weather(url)
    html = w.get_html()
    bs = BeautifulSoup(html,'lxml')
    w.parse_html(bs)

    title = ['合川区最近七天气温数据']
    dates = w.dates
    maxs = w.Maximum_temperature
    mins = w.Minimum_temperature

    w.write_to_file(title,dates,maxs,mins)




