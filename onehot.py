import xlwt
import xlrd
import numpy as np
from numpy.linalg import lstsq
from scipy import stats #/Users/zhengyuting/Downloads/hhh.xlsx
wb = xlrd.open_workbook(filename='/Users/zhengyuting/Downloads/cz.xlsx') #打开文件
print(wb.sheet_names())#获取所有表格名字
sheet = wb.sheet_by_index(2)#通过索引获取表格
tmp_data = sheet.col_values(11)
tmp_gross = sheet.col_values(4)
data = tmp_data[1:]
gross = tmp_gross[1:]
print(tmp_data[1]==12)
print(tmp_gross[1])
onehot = []
log_gross = []
# for x in gross:
#     log_gross.append([x])

IP = 0
for x in data:
    log_gross.append([gross[IP]])
    if x == 1:
        onehot.append([1,0,0,0,0,0,0,0,0,0,0,0])
    elif x == 2:
        onehot.append([1,1,0,0,0,0,0,0,0,0,0,0])
    elif x == 3:
        onehot.append([1,0,1,0,0,0,0,0,0,0,0,0])
    elif x == 4:
        onehot.append([1,0,0,1,0,0,0,0,0,0,0,0])
    elif x == 5:
        onehot.append([1,0,0,0,1,0,0,0,0,0,0,0])
    elif x == 6:
        onehot.append([1,0,0,0,0,1,0,0,0,0,0,0])
    elif x == 7:
        onehot.append([1,0,0,0,0,0,1,0,0,0,0,0])
    elif x == 8:
        onehot.append([1,0,0,0,0,0,0,1,0,0,0,0])
    elif x == 9:
        onehot.append([1,0,0,0,0,0,0,0,1,0,0,0])
    elif x == 10:
        onehot.append([1,0,0,0,0,0,0,0,0,1,0,0])
    elif x == 11:
        onehot.append([1,0,0,0,0,0,0,0,0,0,1,0])
    elif x == 12:
        onehot.append([1,0,0,0,0,0,0,0,0,0,0,1])
    else: 
        log_gross = log_gross[:-1]
        pass
    IP += 1




# IP = 0
# for x in data:
#     log_gross.append([gross[IP]])
#     if x == 'Horror':
#         onehot.append([1,0,0,0])
#     elif x == 'Comedy / Drama':
#         onehot.append([1,0,0.5,0.5])
#     elif x == 'Thriller':
#         onehot.append([1,1,0,0])
#     elif x == 'Comedy':
#         onehot.append([1,0,1,0])
#     elif x == 'Drama':
#         onehot.append([1,0,0,1])
#     else: 
#         log_gross = log_gross[:-1]
#         pass
#     IP += 1
X = np.array(onehot)
y = np.array(log_gross)
# print(len(X), len(y))
print(np.linalg.lstsq(X, y))






# IP = 0
# for x in data:
#     log_gross.append([gross[IP]])
#     if x == 'PG-13':
#         onehot.append([1,0,0,0,0])
#     elif x == 'NC-17':
#         onehot.append([1,1,0,0,0])
#     elif x == 'PG':
#         onehot.append([1,0,1,0,0])
#     elif x == 'R':
#         onehot.append([1,0,0,1,0])
#     elif x == 'G':
#         onehot.append([1,0,0,0,1])
#     else: 
#         log_gross = log_gross[:-1]
#         pass
#     IP += 1
# X = np.array(onehot)
# y = np.array(log_gross)
# print(len(X), len(y))
# print(np.linalg.lstsq(X, y))


# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing as fch  #加载加利福尼亚房屋价值数据
#加载线性回归需要的模块和库
import statsmodels.api as sm #最小二乘
from statsmodels.formula.api import ols #加载ols模型

model = sm.OLS(y,X)
results = model.fit()
print(results.params)
print(results.summary())

#设置全部行输出
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

# data=fch()

# data=fch() #导入数据
# house_data=pd.DataFrame(data.data) #将自变量转换成dataframe格式，便于查看
# house_data.columns=data.feature_names  #命名自变量
# house_data.loc[:,"value"]=data.target #合并自变量，因变量数据
# house_data.shape #查看数据量
# print(house_data.head(10)) #查看前10行数据

# #分训练集测试集
# import random
# random.seed(123) #设立随机数种子
# a=random.sample(range(len(house_data)),round(len(house_data)*0.3))
# house_test=[]
# for i in a:
#     house_test.append(house_data.iloc[i])
# house_test=pd.DataFrame(house_test)
# house_train=house_data.drop(a)

# #重新排列index
# for i in [house_test,house_train]:
#     i.index = range(i.shape[0])
# house_test.head()
# house_train.head()
# house_train = 
# #训练模型
# lm=ols('value~ MedInc + HouseAge + AveRooms + AveBedrms + Population + AveOccup + Latitude + Longitude',data=house_train).fit()

# lm.summary()

# #利用测试集测试模型
# house_test.loc[:,"pread"]=lm.predict(house_test)
# #计算R方
# ##计算残差平方和
# error2=[]
# for i in range(len(house_test)):
#     error2.append((house_test.pread[i]-house_test.loc[:,"value"][i])**2)
# ##计算总离差平方和
# sst=[]
# for i in range(len(house_test)):
#     sst.append((house_test.value[i]-np.mean(house_test.value))**2)
# R2=1-np.sum(error2)/np.sum(sst)
# print("R方为:",R2)

#作预测效果图
# %matplotlib inline
# import matplotlib.pyplot as plt
# plt.plot(range(len(house_test.pread)),sorted(house_test.value),c="black",label= "target_data")
# plt.plot(range(len(house_test.pread)),sorted(house_test.pread),c="red",label = "Predict")
# plt.legend()
# plt.show()

