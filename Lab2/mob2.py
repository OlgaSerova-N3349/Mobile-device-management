import pandas as pd

data=pd.read_excel('DATA.xlsx')

print("Введите множитель тарифного плана k руб/Mb-",end='')
k=int(input())

print("Введите ip-адрес клиента-",end='')
ip=input()

X=k*data[data.IP_Addr==ip].BytesMb.values[0]-k*1
print("Результат тарификации-",X,"руб.")

