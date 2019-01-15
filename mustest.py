import csv
import math

def table(albums_list):

    for item in albums_list:
        print(":",item[0]," "(15-len(item[0])),
        item[1]," "(18-len(item[1])),
        item[2]," "(5-len(item[2])),
        item[3]," "(18-len(item[3])),
        item[4]," "*(13-len(item[4])),)
def import_data_from_file(filename='data.txt'):
    content = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            content.append(line.rstrip('\n').split(','))

    return content

data = []
with open('data.txt', newline='') as inputfile:
    for row in inputfile:
        data.append(row.rstrip("\n").split(","))
        print(row)
# print(data)
# print(len(data[1]))

# for i in data:
    # if int(i[2]) > 1950 :
        # if int(i[2]) < 2000:
            # print(i)

# for i in (data):
    # 
    # print(i)
# gg = []    
# for i in data:
    # i_temp = i[0]
    # i[0] = i[4]
    # i[4] = i_temp
    # gg.append(i[0])
    # print(i)
# gg.sort(reverse=True)
# print(gg)

for i in data:
    time_in_table = i[4].split(":")
    sum_time = (int(time_in_table[0])*60+int(time_in_table[1]))/60
    q = round(sum_time,1)
    print(q)


# for item in data:
    # print("|", item[0], item[1], item[2], item[3], item[4])
    # print("| {:14s} | {:25s} | {:4s} | {:20s} | {:1s} |" .format(item[0], item[1], item[2], item[3], item[4]))


# for item in data:
        # print(":",item[0]," "(15-len(item[0])),
        # item[1]," "(18-len(item[1])),
        # item[2]," "(5-len(item[2])),
        # item[3]," "(18-len(item[3])),
        # item[4]," "*(13-len(item[4])),)