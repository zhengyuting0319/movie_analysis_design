import xlwt
import xlrd
import re

wb = xlrd.open_workbook(filename='movie_data.xlsx') #打开文件
# print(wb.sheet_names())#获取所有表格名字
sheet = wb.sheet_by_index(1)#通过索引获取表格
tmp_data = sheet.col_values(17)
for x in tmp_data:
    if x == '':
        tmp_data = tmp_data[:-1]
col_len = tmp_data.__len__()
director_list = []
for i in range(col_len):
    director = re.findall(r'[\u0041-\u005a\u0061-\u007a\s]+', sheet.cell_value(i,17))
    if director == []:
        continue
    director_list.append(director[0])


wb = xlrd.open_workbook(filename='movie_data.xlsx') #打开文件
# print(wb.sheet_names())#获取所有表格名字
sheet = wb.sheet_by_index(1)#通过索引获取表格
tmp_data = sheet.col_values(1)
for x in tmp_data:
    if x == '':
        tmp_data = tmp_data[:-1]
col_len = tmp_data.__len__()
actor_list = []
for i in range(col_len):
    actor = re.findall(r'[\u0041-\u005a\u0061-\u007a\s]+', sheet.cell_value(i,1))
    if actor == []:
        continue
    actor_list.append(actor[0])
    
famous_distributor = ['UNIVERSAL','PARAMOUNT','PARAMOUNT VANTAGE','PARAMOUNT CLASSICS','PARAMOUNT (DREAMWORKS)','NEW LINE','WARNER BROS.','WARNER BROS. (NEW LINE)','WARNER INDEPENDENT','SONY / SCREEN GEMS','SONY (REVOLUTION)','SONY CLASSICS','SONY BMG','SONY / COLUMBIA','TRISTAR']
wb = xlrd.open_workbook(filename='/Users/zhengyuting/Downloads/1.xlsx') #打开文件
sheet1 = wb.sheet_by_index(0)#通过索引获取表格
data_len = sheet1.col_values(0).__len__()
data = []
for i in range(data_len):
    oscar = 0
    famous = 0
    f_director = 0
    data.append(sheet1.row_values(i))
    actors = data[-1][19].split(',')
    directors = data[-1][18].split(',')
    distributor = data[-1][7]
    for actor in actors:
        if actor in actor_list:
            oscar += 1
    data[-1].append(oscar)
    if distributor in famous_distributor:
        famous += 1
    data[-1].append(famous)
    for director in directors:
        if director in director_list:
            f_director += 1
    data[-1].append(f_director)

print(data[3])


# book = xlwt.Workbook(encoding='utf-8',style_compression=0)
# sheet = book.add_sheet('mysheet',cell_overwrite_ok=True)
# for i in range(len(data)):
#     for j in range(len(data[1])):
#         sheet.write(i,j,data[i][j])
# book.save('/Users/zhengyuting/Desktop/数据与商业分析/Project3/movie_data_with_oscar_actors.xls')
 









# for i in range(col_len):
#     actors = sheet.cell_value(i,19).split(',')
#     for actor in actors:
#         movie_data.append(sheet.row_values(i))
#         movie_data[-1].append(actor)
    
# print(movie_data[0:2])

# book = xlwt.Workbook(encoding='utf-8',style_compression=0)
# sheet = book.add_sheet('mysheet',cell_overwrite_ok=True)
# for i in range(len(movie_data)):
#     for j in range(len(movie_data[1])):
#         sheet.write(i,j,movie_data[i][j])
# book.save('/Users/zhengyuting/Desktop/数据与商业分析/Project3/movie_data_with_actors.xlsx')
 
