import csv
import json
f = open("cleanWeather.json", "r", encoding="UTF-8")
g = open("cleanWeather.csv", "w", newline='')
writer = csv.writer(g)      # 辅助写入
line = f.readline()         # 读取文件中的一行， f.readline()以字符串形式读入
while(line):
    if line == "{\n":       # 遇到 { 开始计数
        count = 8
    if count > 0:           # 计数未停止前，继续向下读取相应行
        line += f.readline()
        count = count - 1   # 计数 - 1
    else:
        dic = json.loads(line)      # 对json进行解析 str->dict
        writer.writerow(dic.values())   # 取出dict中的值，写入到csv文件中
        
        line = f.readline()

f.close()
g.close()

# with open("cleanWeather.csv", "w") as csvfile:
#     while(line):
#         data = []
#         if line[3:13] == "wind_power":
#             count = 9 # 7
#         if count > 0:
#             count = count - 1
#             data.append(line)
#             continue
        
#         line = f.readline()
