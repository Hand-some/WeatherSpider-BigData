#-*- coding: UTF-8 -*- 
f = open("weather.json", 'r',encoding='UTF-8')
g = open("cleanWeather.json", 'w', encoding='UTF-8')
count = 0
line = f.readline()
while line:
    if line[-5:-3] == '风力':
        count = 8
    if count > 0:
        count = count - 1
        # print(line)
        line = f.readline()
        continue
    
    if line[0:2] == '}{':
        line = '}\n{\n'
        # print(line)
    g.write(line)
    line = f.readline()
f.close()
g.close()
