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
file_numbers=["e104","e0105","e108"]
value_array=[]
label_array=[]
for file_number in file_numbers:
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

    
    for i, row in df1.iterrows():
            #print(f"Index: {i}")
            #print(f"{row['start'],row['end'],row['verdict']}")
            value_array+=[[x[row['start']:row['end']].reshape(-1)]]
            label_array+=[[row['verdict']]]
value_array=np.array(value_array)
label_array=np.array(label_array)
print(value_array.shape,label_array.shape)
	
