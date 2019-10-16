import csv
# #s 
# ###为数据添加行首
# headers = ['wind_direction', 'max_t', 'city', 'weather', 'wind_power', 'min_t', 'date']
# f1 = open("new.csv", "w", newline='')  # new_file
# csv.DictWriter(f1,headers).writeheader()
# writer = csv.writer(f1)
# with open("example.csv",'r') as f2:
#     reader = csv.reader(f2)
#     for line in reader:
#         print(line)
#         writer.writerow(line)
# f1.close()
# ###添加行首

# # ###清洗数据
# letters = []
# for a in range(97,123):
#     letters.append(chr(a))
#     letters.append(chr(a-32))
# print(letters)
# f1 = open("clean_abcd.csv", "w", newline='')  # new_file
# writer = csv.writer(f1)
#
# with open("sort_done.csv",'r') as f2:
#     reader = csv.reader( (line.replace('\0','') for line in f2))
#     #i=0
#     for line in reader:
#         if line[1] not in letters:# 清洗ABCD这些无用的索引....
#             writer.writerow(line)
# f1.close()
# # ###清洗数据

# 分割成每个城市的CSV
csv_headers = ['wind_direction', 'city', 'date', 'weather', 'min_t', 'max_t', 'wind_power']
citys = []


def creat_city_file(city_name, line):
    filename = 'D:\\Programs\\Python_Programs\\hello\\Projects\\数据集处理\\data\\' + city_name + '.csv'
    f = open(filename, "a+", newline='', encoding='gb2312')
    writer = csv.writer(f)
    writer.writerow(line)


errors = ['硚口', '瀍河回族', '浉河','猇亭']
with open("clean_abcd.csv", 'r') as f2:
    reader = csv.reader(f2)
    begin = False
    # 获取所有城市列表
    for line in reader:
        # if(line[1] == '瀍河回族'):
        if line[1] == '**':  # 从**城市开始，（跳过该城市），用于程序异常中断时，继续从出错的位置开始，避免重复。
            begin = True
            continue
        if begin:
            path = 'D:\\Programs\\Python_Programs\\hello\\Projects\\数据集处理\\data\\'
            filename = path + line[1] + '.csv'
            fw = open(filename, "a+", newline='', encoding='gb2312')
            writer = csv.writer(fw)
            if line[1] not in citys:
                citys.append(line[1])
                creat_city_file(line[1], line)
            else:  # if line[1] in citys:
                writer.writerow(line)