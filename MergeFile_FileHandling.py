
fr1 = open('files/MyData', 'r')
fr2 = open('files/abc', 'r')

fw = open('files/merge', 'w')

for data in fr1:
    fw.write(data)

for data in fr2:
    fw.write(data)