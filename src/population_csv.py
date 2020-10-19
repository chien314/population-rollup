import csv
import sys

with open(sys.argv[1], 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    newrow=[]
    for row in my_reader:
        newcol=[]
        for i in range(len(row)): 
            newcol.append(row[i])
        newrow.append(newcol)

my_reader = newrow[1:] 
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
    csvwriter = csv.writer(f) 
    csvwriter.writerows(res)
