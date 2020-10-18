import sys

def imp(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
    data = data.strip(' ').split('\n')
    for i in range(len(data)):
        data[i] = data[i].strip(' ').split(',')
        for j in range(len(data[i])):
            data[i][j] = data[i][j].strip(' ')  
    if data[-1]==['']:
        data=data[:-1] 
    data=data[1:]        
    for i in range(len(data)):        
        data[i][8]=data[i][8]+', '+ data[i][9]
        for j in range(10,21):
            data[i][j-1]=data[i][j]
        data[i]=data[i][:-1]
    return data

my_reader = imp(sys.argv[1]) 
    # create a dictionary to count frequency of CBSA09
freq={}
for row in my_reader:
    if len(row[7])!=0:
        if row[7] in freq: # CBSA09 locates at position 7 of each row
            if row[3] not in freq[row[7]][1]:
                freq[row[7]][0]+=1
                freq[row[7]][1].append(row[3])
                freq[row[7]].append([row[8],row[12],row[14]])
        else:
            freq[row[7]]=[1,[row[3]]]
            freq[row[7]].append([row[8],row[12],row[14]])

res=[]
for key,val in freq.items():
    sum=0
    tot_pop_00=0
    tot_pop_10=0
    for i in range(2,val[0]+2):
        sum+=( float(val[i][2])-float(val[i][1]) )/float(val[i][1])
        tot_pop_00 += int(val[i][1])
        tot_pop_10 += int(val[i][2])
    avg=sum/val[0]  
    res.append([key,val[2][0],val[0],tot_pop_00,tot_pop_10,round(avg*100,2)])


with open(sys.argv[2], 'w') as f: 
    for i in range(len(res)):
        for j in range(len(res[i])-1):           
            f.write(str(res[i][j])+',') 
        f.write(str(res[i][len(res[i])-1]))     
        f.write('\n')   


