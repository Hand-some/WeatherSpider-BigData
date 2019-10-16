# WeatherSpider-BigData
华中科技大学计算机科学与技术学院大数据导论数据级爬虫

## 爬取对象：[历史天气网](lishi.tianqi.com)

## 使用架构：Scrapy

## 爬虫运行方式
- `cd WeatherSpider`
- `scrapy crawl historyWeather`

## 其它文件
- trans.py  对爬取后的数据进行整理和清洗
- json2csv.py  将清洗后的数据转为csv文件格式
- cut_csv.py  将大的csv文件按城市切分为多个小文件
- erro_city.py  对csv文件中存在的错误数据进行清洗
