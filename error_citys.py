import csv
# #s
csv_headers = ['wind_direction', 'city', 'date', 'weather', 'min_t', 'max_t', 'wind_power']
citys = []


def creat_city_file(city_name, line):
    filename = 'D:\\Programs\\Python_Programs\\hello\\Projects\\数据集处理\\'+city_name + '.csv'
    f = open(filename, "a+", newline='',encoding='gbk')
    writer = csv.writer(f)
    writer.writerow(line)

errors = ['硚口', '瀍河回族', '浉河','猇亭']
with open("clean_abcd.csv", 'r') as f2:
    reader = csv.reader(f2)
    begin = False
    # 获取所有城市列表
    for line in reader:
        if line[1] in errors:
            begin = True
        else:
            begin = False
        if begin:
            path = 'D:\\Programs\\Python_Programs\\hello\\Projects\\数据集处理\\'
            filename = path + line[1] + '.csv'
            fw = open(filename, "a+", newline='', encoding='gbk')
            if line[1] not in citys:
                citys.append(line[1])
                creat_city_file(line[1], line)
            elif line[1] in citys:
                writer = csv.writer(fw)
                writer.writerow(line)