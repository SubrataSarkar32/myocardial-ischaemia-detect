import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
try:
    import wfdb
except ImportError:
    import pip
    pip.main(['install','matplotlib','wfdb'])
    import wfdb
folder="european-st-t-database"
file_number="e0105"
record = wfdb.rdrecord(os.path.join(folder,file_number)) 
wfdb.plot_wfdb(record=record, title='Record '+file_number+' from European st-t') 
#display(record.__dict__)
blank=0
try:
    df1=pd.read_csv('european-st-t-database-'+file_number+'.csv')
    blank=1
except Exception as e:
    print("File does not exist")
    print("create file")
    with open('european-st-t-database-'+file_number+'.csv', 'w'):
            pass
    df=pd.DataFrame(columns =['start','end','verdict'])
    df.to_csv('european-st-t-database-'+file_number+'.csv', encoding='utf-8', index=False)
df1=pd.read_csv('european-st-t-database-'+file_number+'.csv')
if blank==1:
    tail_rec=df1.tail(1)
    new_start=int(tail_rec.end)
else:
    new_start=0
proceed=1

arr1=np.array(record.p_signal[:])
y, x = arr1.T
x=np.array([y for y in x])
x=x.reshape(-1, 1)
ans_list=[]
while(proceed and new_start<record.sig_len):
    check_region_start=new_start
    check_region_end=new_start+240
    check_region=x[check_region_start:check_region_end]
    ts=np.array([n+1 for n in range(240)])
    plt.plot(ts,check_region)
    plt.show()
    verdict=int(input("Enter verdict for shownn region:(0/1)"))
    ans_list+=[[check_region_start,check_region_end,verdict]]
    proceed=int(input("Do you wish to continue?(0/1)"))
    new_start+=240
df2=pd.DataFrame(ans_list,columns =['start','end','verdict'])
if blank==1:
    final_df=pd.concat([df1, df2])
else:
    final_df=df2
print("Saving file...")
final_df.to_csv('european-st-t-database-'+file_number+'.csv', encoding='utf-8', index=False)
