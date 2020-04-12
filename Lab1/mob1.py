import pandas as pd

data=pd.read_csv('data.csv', index_col='msisdn_origin')

print("Введите номер абонента-",end='')
number=int(input())

print("\nВведите условия тарификации:\nДля исходящих звонков-",end='')
OutCalls=int(input())

print("\nДля входящих звонков-",end='')
InCalls=int(input())

print("\nДля СМС сообщений-",end='')
SMS=int(input())

R=data[data.msisdn_dest==number].call_duration.values[0]

x1=OutCalls*data.loc[number]['call_duration']
x2=InCalls*R

X=x1+x2 

Y=SMS*data.loc[number]['sms_number']

print("\nВходящие-",x1,"\nИсходящие-",x2,"\nТелефония итого-",X,"\nСМС-",Y)




    
   

             

    

    
    
