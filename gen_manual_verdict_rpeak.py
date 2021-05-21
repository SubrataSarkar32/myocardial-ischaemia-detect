import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import math
try:
    import wfdb
except ImportError:
    import pip
    pip.main(['install','matplotlib','wfdb'])
    import wfdb
folder="european-st-t-database"
file_numbers=["e0105"]
value_array=[]
label_array=[]
for file_number in file_numbers:
    record = wfdb.rdrecord(os.path.join(folder,file_number)) 
    wfdb.plot_wfdb(record=record, title='Record '+file_number+' from European st-t') 
    #display(record.__dict__)
    blank=0
    try:
        df1=pd.read_csv('european-st-t-database-'+file_number+'extra.csv')
        blank=1
    except Exception as e:
        print("File does not exist")
        print("create file")
        with open('european-st-t-database-'+file_number+'extra.csv', 'w'):
                pass
        df=pd.DataFrame(columns =['start','end','verdict','max_val','r_peak_bool','angle'])
        df.to_csv('european-st-t-database-'+file_number+'extra.csv', encoding='utf-8', index=False)
    df1=pd.read_csv('european-st-t-database-'+file_number+'.csv')
    

    arr1=np.array(record.p_signal[:])
    y, x = arr1.T
    x=np.array([y for y in x])
    x=x.reshape(-1, 1)
    ans_list=[]

    
    for i, row in df1.iterrows():
            #print(f"Index: {i}")
            #print(f"{row['start'],row['end'],row['verdict']}")
            if row['verdict']==1:
                value_array=[x[row['start']:row['end']].reshape(-1)]
                max_value=max(x[row['start']:row['end']].reshape(-1))
                point=np.where(value_array == max(value_array))[0][0]
                check_region=x[row['start']:row['end']]
                ts=np.array([n+1 for n in range(240)])
                plt.plot(ts,check_region)
                plt.show()
                verdict2=int(input("Enter verdict if given is R peak:(0/1)"))
                if verdict2==1:
                    flag1,flag2=0,0
                    for j in range(point,240):
                        if x[j]<x[j+1]:
                            flag1=1
                            break
                    for k in range(point,0,-1):
                        if x[k-1]>x[k]:
                            flag2=1
                            break
                    if flag2==1:
                        q_point_y=x[k]
                        q_point_x=ts[k]
                    else:
                        q_point_y=x[239]
                        q_point_x=ts[239]
                    if flag1==1:
                        s_point_y=x[j]
                        s_point_x=ts[j]
                    else:
                       s_point_y=x[0]
                       s_point_x=ts[0]
                    r_point_y=max_value
                    r_point_x=point
                    rs_slope=((s_point_y-r_point_y)/(s_point_x-r_point_x))
                    qr_slope=((r_point_y-q_point_y)/(r_point_x-q_point_x))
                    angle=90-(math.degrees(math.atan(qr_slope))-math.degrees(math.atan(rs_slope)))
                else:
                    angle=-1
                ans_list+=[[row['start'],row['end'],row['verdict'],max_value,verdict2,angle]]
                proceed=int(input("Do you wish to continue?(0/1)"))
                if not proceed:
                    break
    df2=pd.DataFrame(ans_list,columns =['start','end','verdict','max_val','r_peak_bool','angle'])
    print("Saving file...")
    df2.to_csv('european-st-t-database-'+file_number+'extra.csv', encoding='utf-8', index=False)
            
