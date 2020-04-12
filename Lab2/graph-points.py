file=open('graph',"r+")
data=file.read()
file.close()
j=0
ch=0
leng=-1;
suma=0
file=open('grep',"r+")

for i in range(len(data)):
    if data[i]==" " and data[i+1]!=" ":
        j+=1
    if j==8 and data[i-1]==" ":
        k=i
        while not data[k]==" ":
            leng+=1
            k+=1
        k=i
        while not data[k]==" ":
            ch+=int(data[k])*pow(10,leng)
            k+=1
            leng-=1
        if ch!=0:
            file.write(str(ch))
            file.write("\n")
            suma+=ch
        ch=0
    if j==9:
        j=0
        
print(suma)

buf=[]
j=0
for i in range(len(data)):
    if data[i]==" " and data[i+1]!=" ":
        j+=1
    if j==1 and data[i-4]=="-":
        k=i
        m=0
        while not data[k]==".":
                buf+=data[k]
                k+=1
        stroka=''.join(buf)
        if len(buf)==8:
            file.write(stroka)
        file.write("\n")
        buf=[]
    if j==9:
        j=0

file.close()



    
