from weather import Weather
from bs4 import BeautifulSoup
import time
from tqdm import tqdm


def main(url,i):
    #创建城市的天气实例
    w = Weather(url)

    #请求url
    html = w.get_html()

    #构建美味的汤的实例
    bs = BeautifulSoup(html,'lxml')

    #解析url
    w.parse_html(bs,html)

    #将数据添加至列表
    dates = w.dates
    maxs = w.Maximum_temperature
    mins = w.Minimum_temperature

    #写入文件
    w.write_to_file(dates,maxs,mins,i)

def make_url(i):
    '''制作每月的url'''
    url = 'http://www.tianqihoubao.com/lishi/chongqing/month/20220'+str(i)+'.html'
    return url


if __name__ == '__main__':
    start_month = 1
    end_month = 7
    #打印进度条
    pbar = tqdm(total=end_month, desc="Count", unit="times")

    #制作每月的url
    for i in range(start_month,end_month+1):
        url = make_url(i)
        main(url, i)
        time.sleep(1)  # 延时1秒
        pbar.update(1)  # 进度条更新

    pbar.close()



